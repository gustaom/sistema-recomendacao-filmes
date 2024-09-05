from src.load_data import load_movies_data, load_ratings_data, process_movie_genres
from src.explore_data import recommend_movies

# Caminhos dos arquivos
movies_path = 'data/ml-1m/movies.dat'
ratings_path = 'data/ml-1m/ratings.dat'

# Carregar dados
movies = load_movies_data(movies_path)
ratings = load_ratings_data(ratings_path)

# Processar os gêneros dos filmes para criar uma matriz de TF-IDF
tfidf_matrix = process_movie_genres(movies)

# Exibir recomendações de filmes para um filme específico (por exemplo, o filme 0)
recommend_movies(0, tfidf_matrix, movies)
