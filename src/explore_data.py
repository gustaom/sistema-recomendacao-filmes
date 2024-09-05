from sklearn.metrics.pairwise import cosine_similarity

def explore_movie_genres(movies):
    print("Gêneros dos filmes:")
    print(movies['genres'].unique())

def recommend_movies(movie_id, tfidf_matrix, movies, top_n=10):
    # Calcular similaridades de cosseno entre os filmes
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Obter índices dos filmes mais similares
    sim_scores = list(enumerate(cosine_sim[movie_id]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Selecionar os top_n filmes mais similares
    top_movies = sim_scores[1:top_n+1]

    # Exibir os títulos dos filmes recomendados
    print(f"Filmes recomendados para o filme {movies.iloc[movie_id]['title']}:")
    for i, score in top_movies:
        print(f"{movies.iloc[i]['title']} - Similaridade: {score}")
