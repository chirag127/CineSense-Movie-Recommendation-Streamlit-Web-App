"""
Initialization file for the data module.
"""

from .preprocessing import create_tfidf_matrix, download_nltk_data

__all__ = ["create_tfidf_matrix", "download_nltk_data"]
