Smart Movie Recommendation System

A web-based movie recommendation application built with Streamlit that uses content-based filtering to suggest movies similar to your favorites. Just pick a movie you like, and the app will recommend 10 similar movies based on their content, genres, and other features.

Project Details

This is a movie recommendation system that analyzes movie features like genres, keywords, cast, and crew to find movies that are similar to the one you select. The recommendations are powered by a machine learning model that uses TF-IDF vectorization and cosine similarity to match movies.

The application uses a dataset containing information about 481 movies, including movie titles, genres, keywords, cast and crew information, ratings, popularity scores, and movie overviews. The system uses pre-computed similarity matrices and a trained TF-IDF vectorizer to provide fast and accurate recommendations.

To run the application, navigate to the project directory and execute the command "streamlit run app.py". The app will automatically open in your default web browser at http://localhost:8501.

Advantages

Smart Recommendations: Get 10 personalized movie recommendations based on content similarity. The system analyzes multiple features to find movies that truly match your preferences.

Fast Performance: Quick recommendations using pre-computed similarity matrices. The app loads instantly and provides results without any delay.

User-Friendly Interface: Clean and modern interface built with Streamlit that makes it easy to select movies and view recommendations.

Detailed Information: View ratings, genres, and overviews for each recommended movie, helping you make informed decisions about what to watch next.

No User Data Required: The system works without requiring user accounts or personal data. Simply select a movie and get recommendations instantly.

Working Process

The recommendation system uses a content-based filtering approach with the following steps:

Data Processing: Movie features like genres, keywords, cast, and crew are extracted and processed from the dataset. The system combines multiple text features to create a comprehensive profile for each movie.

Vectorization: Text features are converted to numerical vectors using TF-IDF (Term Frequency-Inverse Document Frequency). This technique converts text data into a format that can be mathematically compared, giving more weight to important words and less weight to common words.

Similarity Calculation: Cosine similarity is used to compute how similar each movie is to every other movie in the dataset. This creates a similarity matrix where each movie has a similarity score with every other movie, ranging from 0 (completely different) to 1 (very similar).

Recommendation Generation: When you select a movie, the system retrieves the pre-computed similarity scores for that movie, sorts them in descending order, and returns the top 10 most similar movies (excluding the selected movie itself).

The similarity matrix and vectorizer are pre-computed during the model training phase, which means the app can provide instant recommendations without needing to process data in real-time. This makes the application fast and responsive, even with a large dataset of 481 movies.
