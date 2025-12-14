"""
Main Streamlit application for the CineSense Movie Recommendation System.

This module provides a web-based user interface for generating personalized
movie recommendations. It leverages a content-based filtering approach
that uses TF-IDF vectors to represent movie descriptions. The user can
select one or more movies they enjoy, and the system will recommend
similar movies based on cosine similarity of their TF-IDF profiles.

The application is built with Streamlit, an open-source Python library
that makes it easy to create beautiful, custom web apps for machine
learning and data science.

Key Features:
-   Interactive movie selection from a pre-defined list.
-   Adjustable number of recommendations to display.
-   Efficient data loading using Apache Feather format.
-   Caching of loaded data for improved performance.
"""

import pickle
from pathlib import Path
from typing import List, Optional

import pandas as pd
import streamlit as st
from streamlit import session_state as session

from src.recommend.recommend import recommend_table
from src.data.preprocessing import download_nltk_data


def main() -> None:
    """
    Main function to run the Streamlit application.

    This function sets up the user interface, loads the necessary data,
    and handles user interactions to generate and display movie recommendations.
    It is the primary entry point for the application.
    """
    download_nltk_data()
    st.set_page_config(
        page_title="CineSense Movie Recommender",
        page_icon="🎬",
        layout="centered",
        initial_sidebar_state="auto",
    )

    st.title("🎬 CineSense Movie Recommendation System")
    st.markdown(
        "Welcome to **CineSense**! This is a Content-Based Recommender "
        "System that uses implicit ratings to suggest movies you might "
        "like. Select a few movies you've enjoyed, and we'll find some "
        "hidden gems for you! 🍿"
    )

    try:
        tfidf_data = _load_tfidf_data()
        movie_list = _load_movie_list()
    except FileNotFoundError:
        st.error(
            "Could not find the required data files. Please make sure the "
            "`data` directory is properly populated and try again."
        )
        return

    _render_recommendation_form(tfidf_data, movie_list)


@st.cache_data(show_spinner="Loading movie data...")
def _load_tfidf_data() -> pd.DataFrame:
    """
    Loads the TF-IDF data from a Feather file and sets the index.

    This function is cached to prevent reloading the data on every
    interaction with the Streamlit app. The data is loaded from a
-   Feather file for fast and efficient retrieval.

    Returns:
        pd.DataFrame: A DataFrame containing the TF-IDF vectors for each movie,
                      with the movie titles as the index.

    Raises:
        FileNotFoundError: If the `tfidf_data.feather` file does not exist.
    """
    tfidf_path = Path("./data/tfidf_data.feather")
    if not tfidf_path.exists():
        raise FileNotFoundError(f"Could not find TF-IDF data at: {tfidf_path}")
    return pd.read_feather(tfidf_path).set_index("title")


@st.cache_data(show_spinner="Loading movie list...")
def _load_movie_list() -> List[str]:
    """
    Loads the list of movie titles from a pickle file.

    This function is cached to ensure the movie list is loaded only once.
    The list of movies is used to populate the multi-select dropdown in the
    user interface.

    Returns:
        List[str]: A list of movie titles.

    Raises:
        FileNotFoundError: If the `movie_list.pickle` file does not exist.
    """
    movie_list_path = Path("./data/movie_list.pickle")
    if not movie_list_path.exists():
        raise FileNotFoundError(f"Could not find movie list at: {movie_list_path}")
    with movie_list_path.open("rb") as f:
        return pickle.load(f)


def _render_recommendation_form(
    tfidf_data: pd.DataFrame, movie_list: List[str]
) -> None:
    """
    Renders the recommendation form and displays the results.

    This function creates the user interface elements for selecting movies
    and specifying the number of recommendations. It also handles the
    "Recommend" button click event to generate and display the recommended
    movies in a table.

    Args:
        tfidf_data (pd.DataFrame): The TF-IDF data for all movies.
        movie_list (List[str]): The list of available movie titles.
    """
    st.subheader("Step 1: Select Your Favorite Movies")
    session.options = st.multiselect(
        label="Start typing to select one or more movies you've enjoyed:",
        options=movie_list,
        help="Select at least one movie to get recommendations.",
    )

    st.subheader("Step 2: Choose the Number of Recommendations")
    session.slider_count = st.slider(
        label="How many movies would you like us to recommend?",
        min_value=5,
        max_value=50,
        value=10,
        help="Use the slider to set the number of recommendations.",
    )

    st.markdown("---")

    buffer1, col1, buffer2 = st.columns([1.45, 1, 1])
    is_clicked = col1.button(
        label="✨ Get Recommendations",
        type="primary",
        use_container_width=True,
    )

    if is_clicked:
        if not session.options:
            st.warning("Please select at least one movie to get recommendations.")
            return

        with st.spinner("Finding the best movies for you..."):
            recommendations = recommend_table(
                list_of_movie_enjoyed=session.options,
                movie_count=session.slider_count,
                tfidf_data=tfidf_data,
            )

        if recommendations is not None and not recommendations.empty:
            st.success(
                f"Here are your top {session.slider_count} movie recommendations:"
            )
            st.table(recommendations)
        else:
            st.info(
                "Could not find any recommendations based on your selection. "
                "Please try selecting different movies."
            )


if __name__ == "__main__":
    main()
