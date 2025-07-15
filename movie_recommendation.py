from utils import load_datasets, clean_data, build_similarity_matrix, recommend_movies

# Step 1: Load datasets
movies, ratings = load_datasets()

# Step 2: Clean the data
movies = clean_data(movies)

# Step 3: Build similarity matrix
cosine_sim = build_similarity_matrix(movies)

# Step 4: Ask for user input
movie_title = input("Enter a movie title for recommendations: ")

# Step 5: Get recommendations
recommendations = recommend_movies(movie_title, movies, cosine_sim)

# Step 6: Display recommendations
print("\nRecommended Movies:")
for i, rec in enumerate(recommendations, 1):
    print(f"{i}. {rec}")
