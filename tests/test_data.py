"""
Unit tests for the data preprocessing module.
"""

import pandas as pd
import nltk
from src.data.preprocessing import create_tfidf_matrix

def setup_module(module):
    """
    Download NLTK data before running tests.
    """
    nltk.download('punkt')
    nltk.download('stopwords')

def test_create_tfidf_matrix():
    """
    Test the create_tfidf_matrix function.
    """
    data = {'title': ['Movie 1', 'Movie 2', 'Movie 3'],
            'description': ['This is a great movie with a great plot', 'This is another great movie with an even better plot', 'This is a third movie with a different plot']}
    df = pd.DataFrame(data)
    tfidf_df, _ = create_tfidf_matrix(df, 'description', 'title')
    assert tfidf_df.shape[0] == 3
