🎬 Movie Recommender System
A sleek, web-based movie recommendation system built with Streamlit and powered by a content-based filtering algorithm. Enter a movie you like, and get a list of 20 similar movies with their posters!

➡️ View Live Demo Here https://movierecommendationbyrishi.streamlit.app/

<img width="1913" height="965" alt="Screenshot 2025-09-29 131238" src="https://github.com/user-attachments/assets/f9e00bf1-6280-4a9e-aab1-7b82d1c6013f" />

🌟 About The Project
This application provides a user-friendly interface to discover new movies based on your interests. The core of the project is a recommendation engine that suggests films with similar content attributes, such as genres, keywords, and cast. The front end is designed to be visually appealing, featuring a dynamic background and a modern "frosted glass" theme.

✨ Features
Intuitive UI: Select a movie from a dropdown list of 5,000+ titles.

Content-Based Filtering: Recommendations are generated using TF-IDF vectorization and Cosine Similarity.

Dynamic Poster Fetching: Movie posters are fetched in real-time from the OMDb API.

Stylish & Responsive: A modern, Netflix-inspired theme with a blurred background that looks great on any device.

Large File Handling: Utilizes Git LFS to manage the large similarity model file.

🛠️ Technologies Used
Frontend: Streamlit

Backend & Data Processing: Python, Pandas, Scikit-learn

Data: The Movie Database (TMDB 5000 Movie Dataset)

API: OMDb API for fetching movie posters

Version Control: Git & Git LFS

⚙️ How It Works
The recommendation engine is built on a content-based filtering model. Key steps in the process include:

Data Preprocessing: Movie data (genres, keywords, cast, crew) is cleaned and combined into a single "tags" string for each movie.

Vectorization: The "tags" are converted into a numerical vector space using the TF-IDF (Term Frequency-Inverse Document Frequency) technique.

Similarity Calculation: The cosine similarity is calculated between the vector of the user's chosen movie and all other movies in the dataset.

Recommendation: The top 20 movies with the highest similarity scores are selected and displayed to the user.

🙏 Acknowledgements
Dataset provided by The Movie Database (TMDB).

App deployed using the free Streamlit Community Cloud.

👤 Contact - hariom231b125@gmail.com / +918859321534
HARIOM YADAV - https://github.com/HARIOM8859
