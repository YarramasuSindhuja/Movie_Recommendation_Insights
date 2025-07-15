# Movie Recommendation Insights

A simple Python-based movie recommendation system that suggests similar movies based on genres and user ratings.

## Features
- Loads and cleans movie and rating datasets
- Computes movie similarity using genres
- Recommends movies based on a given title
- Simple command-line interface

## Requirements
- Python 3.7+
- pandas
- scikit-learn

Install dependencies:
```bash
pip install pandas scikit-learn
```

## Usage
Run the main script and follow the prompt:
```bash
python movie_recommendation.py
```
Enter a movie title when prompted to get recommendations.

## Data Files
- Place your CSV files (`movie.csv`, `rating.csv`, etc.) in the project directory.
- **Note:** Large files like `rating.csv` and `genome_scores.csv` are NOT tracked in git. If you need these files, download them from [MovieLens](https://grouplens.org/datasets/movielens/) or your own source.

## Project Structure
```
Movie_Recommendation_Insights/
├── movie_recommendation.py
├── utils.py
├── movie.csv
├── rating.csv
├── ...
```

## License
MIT
