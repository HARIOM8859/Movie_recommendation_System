# Movie_recommendation_System
This is a content-based movie recommendation system built using metadata from the TMDB (The Movie Database) dataset. The system recommends similar movies by analyzing and comparing features like genres, keywords, cast, crew, and movie overviews.
# Features
Merges movie and credit datasets from TMDB.
Parses and cleans nested JSON fields.
Extracts important metadata: genres, keywords, top 3 cast members, and director.
Combines all relevant textual information into a single tags column.
Applies text preprocessing: lowercasing, stemming, and stopword removal.
Transforms text into numerical vectors using CountVectorizer (Bag of Words).
Computes similarity using cosine similarity.
Recommends top 5 similar movies based on user input.
Stores processed data and similarity matrix using pickle for reuse.

# Datasets Used
tmdb_5000_movies.csv
tmdb_5000_credits.csv
Both datasets were obtained from Kaggle and merged on the movie title.

# Technologies and Libraries
Python
Pandas
NumPy
ast
NLTK
Scikit-learn
Pickle

# Project Workflow
Data Loading and Merging-
The two datasets are merged on the title column to consolidate movie and credit information.
Feature Engineering-
Important features such as genres, keywords, cast, and crew are extracted. Only the top 3 cast members and the director are retained to keep it concise.
Tag Creation-
All relevant textual data is combined into a single column called tags.
Text Preprocessing-
Tags are cleaned by converting to lowercase and applying stemming using NLTK's PorterStemmer.
Vectorization-
The processed tags are vectorized using CountVectorizer with a maximum feature limit and English stopword removal.
Similarity Calculation-
Cosine similarity is computed between movie vectors to identify similar movies.
Recommendation Function-
A function takes a movie title and returns the top 5 most similar movies based on cosine similarity.
