"""
Unit tests for the recommendation module.
"""

import pandas as pd
from src.recommend.recommend import recommend_table

def test_recommend_table():
    """
    Test the recommend_table function.
    """
    data = {'movie1': [1, 0, 0], 'movie2': [0, 1, 0], 'movie3': [1, 1, 0], 'movie4': [0, 0, 1]}
    tfidf_data = pd.DataFrame(data, index=['feature1', 'feature2', 'feature3']).T
    recommendations = recommend_table(['movie1'], tfidf_data, movie_count=1)
    assert recommendations.index[0] == 'movie3'

def test_recommend_table_empty_input():
    """
    Test the recommend_table function with an empty input list.
    """
    data = {'movie1': [1, 0, 0], 'movie2': [0, 1, 0], 'movie3': [1, 1, 0], 'movie4': [0, 0, 1]}
    tfidf_data = pd.DataFrame(data, index=['feature1', 'feature2', 'feature3']).T
    recommendations = recommend_table([], tfidf_data)
    assert recommendations is None
