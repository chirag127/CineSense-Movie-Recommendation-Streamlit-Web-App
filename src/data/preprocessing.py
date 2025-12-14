"""
Data preprocessing module for the CineSense Movie Recommendation System.

This module provides functions for cleaning and transforming the raw movie
dataset into a format suitable for TF-IDF vectorization. The primary
functions in this module are responsible for cleaning the movie
descriptions by removing irrelevant characters and stopwords, and then
vectorizing the cleaned text into a TF-IDF matrix.

The preprocessing steps are crucial for ensuring the quality of the
recommendations, as they directly impact the feature representation of
the movies. By creating a clean and informative TF-IDF matrix, we can
more accurately measure the similarity between movies.

Key Functions:
-   `create_tfidf_matrix`: Generates a TF-IDF matrix from a DataFrame of
    movie data.
"""

import re
from typing import List, Tuple

import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer


def download_nltk_data() -> None:
    """
    Downloads the required NLTK data for tokenization and stopwords.

    This function checks if the `punkt` and `stopwords` packages are
    available, and if not, it downloads them. This is a necessary setup
    step to ensure that the text cleaning functions can work correctly.
    """
    try:
        nltk.data.find("tokenizers/punkt")
    except nltk.downloader.DownloadError:
        nltk.download("punkt")
    try:
        nltk.data.find("corpora/stopwords")
    except nltk.downloader.DownloadError:
        nltk.download("stopwords")


def create_tfidf_matrix(
    dataset: pd.DataFrame, desc_col: str, item_col: str
) -> Tuple[pd.DataFrame, TfidfVectorizer]:
    """
    Creates a TF-IDF matrix from a given dataset.

    This function takes a DataFrame containing movie data and generates a
    TF-IDF matrix from the specified description column. The TF-IDF matrix
    represents the importance of each word in each movie's description,
    which is then used to calculate movie similarity.

    Args:
        dataset (pd.DataFrame): The DataFrame containing the movie data.
        desc_col (str): The name of the column with the movie descriptions.
        item_col (str): The name of the column with the movie titles or IDs.

    Returns:
        Tuple[pd.DataFrame, TfidfVectorizer]: A tuple containing the
            generated TF-IDF matrix as a DataFrame and the fitted
            `TfidfVectorizer` object.
    """
    if not all(col in dataset.columns for col in [desc_col, item_col]):
        raise ValueError(
            "The specified description and item columns are not in the DataFrame."
        )

    tfidf = TfidfVectorizer(min_df=2, max_df=0.7, stop_words="english")
    tfidf_vectors = tfidf.fit_transform(dataset[desc_col])

    tfidf_df = pd.DataFrame(
        tfidf_vectors.toarray(),
        columns=tfidf.get_feature_names_out(),
        index=dataset[item_col],
    )

    return tfidf_df, tfidf
