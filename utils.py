import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.metrics.pairwise import cosine_similarity

# Function to load datasets
def load_datasets():
    # Load movies and ratings dataset
    movies = pd.read_csv('movie.csv')  # Updated to match actual file name
    ratings = pd.read_csv('rating.csv')  # Updated to match actual file name
    return movies, ratings

# Function to clean data
def clean_data(movies):
    # Drop missing values in critical columns
    movies.dropna(subset=['title', 'genres'], inplace=True)
    return movies

# Function to build cosine similarity matrix
def build_similarity_matrix(movies):
    # Use the genres column to calculate similarity
    count_vectorizer = CountVectorizer(stop_words='english')
    count_matrix = count_vectorizer.fit_transform(movies['genres'])
    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    return cosine_sim

# Function to recommend movies
def recommend_movies(title, movies, cosine_sim):
    try:
        # Find the index of the movie
        idx = movies[movies['title'] == title].index[0]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:11]  # Top 10 similar movies
        movie_indices = [i[0] for i in sim_scores]
        return movies['title'].iloc[movie_indices].tolist()
    except IndexError:
        return ["Movie not found! Please check the title."]
