"""
Recommendation module for the CineSense Movie Recommendation System.

This module contains the core logic for generating movie recommendations
based on a user's movie preferences. The recommendation process is
centered around the concept of creating a user profile from the movies
they have enjoyed, and then comparing this profile to other movies in the
dataset to find the most similar ones.

The similarity is calculated using the cosine similarity of the TF-IDF
vectors of the movies. By averaging the TF-IDF vectors of the movies a
user likes, we create a "user profile" vector that represents their
tastes. This profile is then used to find movies that are closest to it
in the vector space.

Key Functions:
-   `recommend_table`: The main function for generating movie recommendations.
"""

from typing import List, Optional

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def recommend_table(
    list_of_movie_enjoyed: List[str],
    tfidf_data: pd.DataFrame,
    movie_count: int = 20,
) -> Optional[pd.DataFrame]:
    """
    Generates a table of recommended movies based on a list of enjoyed movies.

    This function takes a list of movies that a user has enjoyed and
    recommends a specified number of new movies based on their similarity.
    The similarity is calculated by creating a user profile from the
    TF-IDF vectors of the enjoyed movies and then finding the movies with
    the highest cosine similarity to this profile.

    Args:
        list_of_movie_enjoyed (List[str]): A list of movie titles that the
            user has enjoyed.
        tfidf_data (pd.DataFrame): The DataFrame containing the TF-IDF
            vectors for all movies.
        movie_count (int, optional): The number of movies to recommend.
            Defaults to 20.

    Returns:
        Optional[pd.DataFrame]: A DataFrame containing the recommended
            movies and their similarity scores, sorted in descending order.
            Returns `None` if the list of enjoyed movies is empty or if no
            recommendations can be generated.
    """
    if not list_of_movie_enjoyed:
        return None

    try:
        movie_enjoyed_df = tfidf_data.reindex(list_of_movie_enjoyed)
        user_prof = movie_enjoyed_df.mean()
    except KeyError:
        # This can happen if the movie titles are not in the TF-IDF data
        return None

    tfidf_subset_df = tfidf_data.drop(list_of_movie_enjoyed, errors="ignore")

    if tfidf_subset_df.empty:
        return None

    similarity_array = cosine_similarity(
        user_prof.values.reshape(1, -1), tfidf_subset_df
    )

    similarity_df = pd.DataFrame(
        similarity_array.T,
        index=tfidf_subset_df.index,
        columns=["similarity_score"],
    )

    sorted_similarity_df = similarity_df.sort_values(
        by="similarity_score", ascending=False
    ).head(movie_count)

    return sorted_similarity_df
