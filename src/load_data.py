import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def load_movies_data(path):
    return pd.read_csv(path, sep='::', engine='python', header=None, names=['movie_id', 'title', 'genres'], encoding='ISO-8859-1')

def load_ratings_data(path):
    return pd.read_csv(path, sep='::', engine='python', header=None, names=['user_id', 'movie_id', 'rating', 'timestamp'], encoding='ISO-8859-1')

def process_movie_genres(movies):
    # Processar os gêneros dos filmes para criar uma matriz TF-IDF
    tfidf = TfidfVectorizer(token_pattern=r'[^|]+')  # O token é separado pelo símbolo '|'
    tfidf_matrix = tfidf.fit_transform(movies['genres'])
    return tfidf_matrix
