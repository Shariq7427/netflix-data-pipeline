import streamlit as st
import pandas as pd
import plotly.express as px
import os

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Netflix Analytics Dashboard",
    page_icon="🎬",
    layout="wide"
)

# =====================================================
# LOAD DATA
# =====================================================

@st.cache_data
def load_data():

    # Project root directory
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # CSV file location
    file_path = os.path.join(
        base_dir,
        "data",
        "netflix_titles.csv.csv"
    )

    # Read dataset
    df = pd.read_csv(file_path)

    # Fill missing values
    df["country"] = df["country"].fillna("Unknown")
    df["listed_in"] = df["listed_in"].fillna("Unknown")
    df["rating"] = df["rating"].fillna("Unknown")
    df["director"] = df["director"].fillna("Unknown")

    return df


# Load dataframe
df = load_data()

# =====================================================
# ALL COUNTRIES
# =====================================================

all_countries = []

for countries in df["country"]:
    all_countries.extend(
        [c.strip() for c in str(countries).split(",")]
    )

all_countries = sorted(list(set(all_countries)))

# =====================================================
# ALL GENRES
# =====================================================

all_genres = []

for genres in df["listed_in"]:
    all_genres.extend(
        [g.strip() for g in str(genres).split(",")]
    )

all_genres = sorted(list(set(all_genres)))

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("🎬 Netflix Filters")

selected_countries = st.sidebar.multiselect(
    "Countries",
    all_countries
)

selected_genres = st.sidebar.multiselect(
    "Genres",
    all_genres
)

selected_type = st.sidebar.multiselect(
    "Content Type",
    df["type"].unique(),
    default=df["type"].unique()
)

selected_rating = st.sidebar.multiselect(
    "Ratings",
    sorted(df["rating"].unique())
)

# =====================================================
# FILTERING
# =====================================================

filtered_df = df.copy()

if selected_countries:

    filtered_df = filtered_df[
        filtered_df["country"].apply(
            lambda x: any(
                country in [c.strip() for c in str(x).split(",")]
                for country in selected_countries
            )
        )
    ]

if selected_genres:

    filtered_df = filtered_df[
        filtered_df["listed_in"].apply(
            lambda x: any(
                genre in [g.strip() for g in str(x).split(",")]
                for genre in selected_genres
            )
        )
    ]

if selected_type:

    filtered_df = filtered_df[
        filtered_df["type"].isin(selected_type)
    ]

if selected_rating:

    filtered_df = filtered_df[
        filtered_df["rating"].isin(selected_rating)
    ]

# =====================================================
# HEADER
# =====================================================

st.title("🎬 Netflix Analytics Dashboard")
st.markdown(
    "Interactive dashboard using the Netflix Kaggle Dataset"
)

# =====================================================
# KPI CARDS
# =====================================================

total_titles = len(filtered_df)

movies = len(
    filtered_df[
        filtered_df["type"] == "Movie"
    ]
)

tv_shows = len(
    filtered_df[
        filtered_df["type"] == "TV Show"
    ]
)

countries_count = len(all_countries)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Titles", f"{total_titles:,}")
col2.metric("Movies", f"{movies:,}")
col3.metric("TV Shows", f"{tv_shows:,}")
col4.metric("Countries", countries_count)

st.divider()

# =====================================================
# MOVIES VS TV SHOWS
# =====================================================

type_counts = (
    filtered_df["type"]
    .value_counts()
    .reset_index()
)

type_counts.columns = ["Type", "Count"]

fig_type = px.pie(
    type_counts,
    names="Type",
    values="Count",
    hole=0.5,
    title="Movies vs TV Shows"
)

# =====================================================
# TOP COUNTRIES
# =====================================================

country_df = filtered_df.copy()

country_df["country"] = (
    country_df["country"]
    .str.split(",")
)

country_df = country_df.explode("country")

country_df["country"] = (
    country_df["country"]
    .str.strip()
)

country_counts = (
    country_df["country"]
    .value_counts()
    .head(15)
    .reset_index()
)

country_counts.columns = ["Country", "Count"]

fig_country = px.bar(
    country_counts,
    x="Country",
    y="Count",
    title="Top Countries by Content"
)

left, right = st.columns(2)

with left:
    st.plotly_chart(
        fig_type,
        use_container_width=True
    )

with right:
    st.plotly_chart(
        fig_country,
        use_container_width=True
    )

# =====================================================
# RELEASE YEAR TREND
# =====================================================

year_counts = (
    filtered_df["release_year"]
    .value_counts()
    .sort_index()
    .reset_index()
)

year_counts.columns = ["Year", "Count"]

fig_year = px.line(
    year_counts,
    x="Year",
    y="Count",
    markers=True,
    title="Netflix Content Growth Over Time"
)

st.plotly_chart(
    fig_year,
    use_container_width=True
)

# =====================================================
# TOP GENRES
# =====================================================

genre_df = filtered_df.copy()

genre_df["listed_in"] = (
    genre_df["listed_in"]
    .str.split(",")
)

genre_df = genre_df.explode("listed_in")

genre_df["listed_in"] = (
    genre_df["listed_in"]
    .str.strip()
)

genre_counts = (
    genre_df["listed_in"]
    .value_counts()
    .head(15)
    .reset_index()
)

genre_counts.columns = ["Genre", "Count"]

fig_genre = px.bar(
    genre_counts,
    x="Genre",
    y="Count",
    title="Top Genres"
)

st.plotly_chart(
    fig_genre,
    use_container_width=True
)

# =====================================================
# RATINGS
# =====================================================

rating_counts = (
    filtered_df["rating"]
    .value_counts()
    .head(15)
    .reset_index()
)

rating_counts.columns = ["Rating", "Count"]

fig_rating = px.bar(
    rating_counts,
    x="Rating",
    y="Count",
    title="Ratings Distribution"
)

st.plotly_chart(
    fig_rating,
    use_container_width=True
)

# =====================================================
# TOP DIRECTORS
# =====================================================

director_counts = (
    filtered_df["director"]
    .value_counts()
    .head(15)
    .reset_index()
)

director_counts.columns = ["Director", "Count"]

fig_director = px.bar(
    director_counts,
    x="Director",
    y="Count",
    title="Top Directors"
)

st.plotly_chart(
    fig_director,
    use_container_width=True
)

# =====================================================
# SEARCH
# =====================================================

st.subheader("🔍 Search Netflix Titles")

search = st.text_input("Search Title")

if search:

    results = filtered_df[
        filtered_df["title"]
        .str.contains(
            search,
            case=False,
            na=False
        )
    ]

    st.dataframe(
        results,
        use_container_width=True
    )

# =====================================================
# DATASET VIEW
# =====================================================

with st.expander("View Dataset"):
    st.dataframe(
        filtered_df,
        use_container_width=True
    )