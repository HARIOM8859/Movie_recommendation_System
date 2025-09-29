import streamlit as st
import pickle
import pandas as pd
import requests
import urllib.parse
import base64

# --- CONFIGURATION ---
OMDB_API_KEY = "31a90358"
PLACEHOLDER = "https://via.placeholder.com/300x450?text=No+Image"
BACKGROUND_IMAGE_FILE = "background.jpg"


# --- HELPER FUNCTIONS ---
@st.cache_data
def get_img_as_base64(file):
    try:
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        st.error(f"Background image file not found: {file}")
        return None


def fetch_poster_by_title(title: str) -> str:
    try:
        encoded = urllib.parse.quote(title)
        url = f"http://www.omdbapi.com/?t={encoded}&apikey={OMDB_API_KEY}"
        r = requests.get(url, timeout=6)
        r.raise_for_status()
        data = r.json()
        poster = data.get("Poster")
        if data.get("Response") == "True" and poster and poster != "N/A":
            return poster
    except Exception:
        pass
    return PLACEHOLDER


def recommend(movie: str):
    try:
        movie_index = movies[movies['title'] == movie].index[0]
    except (IndexError, KeyError):
        return [], []
    distances = similarity[movie_index]
    top = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:21]
    names, posters = [], []
    for i, _ in top:
        title = movies.iloc[i].title
        names.append(title)
        posters.append(fetch_poster_by_title(title))
    return names, posters


# --- LOAD DATA ---
try:
    movies = pickle.load(open("movies.pkl", "rb"))
    similarity = pickle.load(open("similarity.pkl", "rb"))
except FileNotFoundError:
    st.error("Model files (movies.pkl or similarity.pkl) not found.")
    st.stop()


# --- STYLING & THEME ---
def apply_styling():
    img = get_img_as_base64(BACKGROUND_IMAGE_FILE)
    if not img:
        return

    styling = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');

    .stApp {{
        background-image: url("data:image/jpeg;base64,{img}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .stApp::before {{
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background-color: rgba(0, 0, 0, 0.7);
        backdrop-filter: blur(3px);
    }}
    [data-testid="stAppViewContainer"] > .main {{
        background-color: transparent;
    }}
    /* --- SHIFT CONTENT UP --- */
    [data-testid="block-container"] {{
        padding-top: 0rem; /* Reduced from 2rem */
        padding-bottom: 2rem;
    }}
    [data-testid="stHeader"] {{
        background: transparent;
    }}

    /* --- UPDATED TITLE STYLE --- */
    .main-title-container {{
        font-family: 'Poppins', sans-serif;
        font-weight: 800;
        text-align: center;
        font-size: 4.5rem;
        filter: drop-shadow(3px 3px 10px rgba(0,0,0,0.8));
        display: flex;
        justify-content: center;
        align-items: center;
        padding-top: 1.5rem; /* Add some space back at the top */
        white-space: nowrap; /* Prevents the title from wrapping to a new line */
    }}

    .title-emoji {{
        /* The emoji will have its default color, no special styling needed */
        margin-right: 1rem;
    }}

    .title-text {{
        background-image: url("data:image/jpeg;base64,{img}");
        background-size: cover;
        background-position: center;
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent !important;
    }}

    div[data-testid="stSpinner"] > div {{
        color: #FFFFFF !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        font-size: 1.1rem;
    }}
    .stSelectbox label {{
        color: #E0E0E0 !important;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.5);
    }}
    div[data-baseweb="select"] > div {{
        background-color: rgba(30, 30, 30, 0.8) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 8px !important;
        color: #FFFFFF !important;
    }}
    .stButton button {{
        background: linear-gradient(90deg, #00AEEF, #008FCC);
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
        border: none;
        font-weight: 600;
        font-family: 'Poppins', sans-serif;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 174, 239, 0.4);
    }}
    .stButton button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 174, 239, 0.6);
    }}
    .movie-card {{
        background-color: rgba(42, 42, 42, 0.8);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        height: 100%;
    }}
    .movie-card:hover {{
        transform: scale(1.05);
        box-shadow: 0 8px 30px rgba(0,0,0,0.5);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }}
    .movie-card img {{
        width: 100%;
        border-radius: 8px;
        margin-bottom: 0.75rem;
    }}
    .movie-card p {{
        font-family: 'Poppins', sans-serif;
        color: #FFFFFF;
        font-weight: 600;
        font-size: 1rem;
        line-height: 1.3;
    }}
    </style>
    """
    st.markdown(styling, unsafe_allow_html=True)


# --- UI LAYOUT ---
apply_styling()

# --- RESTRUCTURED TITLE ---
st.markdown("""
<div class="main-title-container">
    <span class="title-emoji">🎬</span>
    <span class="title-text">Movie Recommender</span>
</div>
""", unsafe_allow_html=True)

selected_movie = st.selectbox(
    "Type or select a movie to get recommendations",
    movies['title'].values,
    label_visibility="collapsed"
)

if st.button("Recommend"):
    with st.spinner('Curating your movie night...'):
        names, posters = recommend(selected_movie)

    if not names:
        st.error("Sorry, no recommendations found for this movie.")
    else:
        st.write("")  # Spacer
        for i in range(0, len(names), 5):
            cols = st.columns(5)
            for j in range(5):
                idx = i + j
                if idx < len(names):
                    with cols[j]:
                        st.markdown(
                            f"""
                            <div class="movie-card">
                                <img src="{posters[idx]}" alt="{names[idx]} poster">
                                <p>{names[idx]}</p>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

