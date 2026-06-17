import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="Netflix Streaming Analytics",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------

st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
    background-color:#0b0f19;
    color:white;
}

[data-testid="stSidebar"]{
    background-color:#111827;
}

.metric-card{
    background:#161b22;
    padding:20px;
    border-radius:15px;
    text-align:center;
    border:1px solid #222;
}

.big-title{
    font-size:38px;
    font-weight:bold;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

with st.sidebar:

    st.markdown(
        "<h1 style='color:#E50914'>NETFLIX</h1>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.button("🏠 Overview")
    st.button("📊 Content Performance")
    st.button("👥 User Activity")
    st.button("📱 Devices")
    st.button("🌍 Geography")
    st.button("💳 Subscriptions")
    st.button("📑 Reports")
    st.button("⚙ Settings")

# -------------------------------------------------
# HEADER
# -------------------------------------------------

st.markdown(
"""
<div class='big-title'>
STREAMING ANALYTICS DASHBOARD
</div>
""",
unsafe_allow_html=True
)

st.caption(
    "Real-time insights into user behavior and content performance"
)

# -------------------------------------------------
# DATA
# -------------------------------------------------

try:
    df = pd.read_csv("netflix_dashboard_data.csv")
except:
    df = pd.read_csv("./netflix_dashboard_data.csv")

# -------------------------------------------------
# KPI CARDS
# -------------------------------------------------

c1,c2,c3,c4,c5 = st.columns(5)

cards = [
("⏱","Total Watch Time","12,450"),
("👥","Active Users","8,752"),
("👁","Total Views","24,350"),
("🕒","Avg Watch Time","67.3"),
("📈","Completion Rate","78.6%")
]

for col,data in zip([c1,c2,c3,c4,c5],cards):

    icon,title,val = data

    col.markdown(f"""
    <div class='metric-card'>
        <h2>{icon}</h2>
        <h4>{title}</h4>
        <h2>{val}</h2>
    </div>
    """,
    unsafe_allow_html=True)

st.write("")

# -------------------------------------------------
# ROW 1
# -------------------------------------------------

col1,col2,col3 = st.columns([1.2,1.2,1])

# -------------------------
# MOST WATCHED CONTENT
# -------------------------

with col1:

    st.subheader("Most Watched Content")

    content = pd.DataFrame({
        "title":[
            "Stranger Things",
            "Money Heist",
            "Wednesday",
            "The Witcher",
            "Bridgerton"
        ],
        "views":[2450,2150,1890,1650,1230]
    })

    fig = px.bar(
        content,
        x="views",
        y="title",
        orientation="h",
        template="plotly_dark",
        color_discrete_sequence=["#E50914"]
    )

    fig.update_layout(
        paper_bgcolor="#161b22",
        plot_bgcolor="#161b22"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# -------------------------
# WATCH TIME TREND
# -------------------------

with col2:

    st.subheader("Watch Time Over Time")

    trend = pd.DataFrame({
        "Day":range(1,32),
        "Hours":np.random.randint(
            900,
            2200,
            31
        )
    })

    fig = px.line(
        trend,
        x="Day",
        y="Hours",
        template="plotly_dark"
    )

    fig.update_traces(
        line_color="#E50914"
    )

    fig.update_layout(
        paper_bgcolor="#161b22",
        plot_bgcolor="#161b22"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# -------------------------
# DONUT CHART
# -------------------------

with col3:

    st.subheader("Top Genres")

    genre = pd.DataFrame({
        "Genre":[
            "Drama",
            "Thriller",
            "Comedy",
            "Action",
            "Documentary"
        ],
        "Share":[35,25,15,15,10]
    })

    fig = px.pie(
        genre,
        names="Genre",
        values="Share",
        hole=0.55,
        template="plotly_dark"
    )

    fig.update_layout(
        paper_bgcolor="#161b22"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# -------------------------------------------------
# ROW 2
# -------------------------------------------------

col4,col5,col6 = st.columns([1.2,1,1])

# -------------------------
# HEATMAP
# -------------------------

with col4:

    st.subheader(
        "User Activity Heatmap"
    )

    heat = np.random.randint(
        0,
        100,
        size=(7,24)
    )

    fig,ax = plt.subplots(
        figsize=(8,3)
    )

    sns.heatmap(
        heat,
        cmap="Reds",
        ax=ax
    )

    st.pyplot(fig)

# -------------------------
# DEVICE USAGE
# -------------------------

with col5:

    st.subheader("Devices Used")

    d1,d2 = st.columns(2)

    d1.metric("📱 Mobile","45%")
    d1.metric("💻 Desktop","15%")

    d2.metric("📺 TV","30%")
    d2.metric("📲 Tablet","10%")

# -------------------------
# COUNTRY MAP
# -------------------------

with col6:

    st.subheader("Top Countries")

    country = pd.DataFrame({
        "country":[
            "United States",
            "India",
            "Brazil",
            "United Kingdom",
            "Canada"
        ],
        "views":[8200,4600,2900,2100,1700]
    })

    fig = px.choropleth(
        country,
        locations="country",
        locationmode="country names",
        color="views",
        template="plotly_dark"
    )

    fig.update_layout(
        paper_bgcolor="#161b22"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# -------------------------------------------------
# INSIGHTS
# -------------------------------------------------

st.markdown("---")

st.subheader("Key Insights")

i1,i2,i3,i4,i5 = st.columns(5)

i1.success("Watch time +12.5%")
i2.info("Weekend engagement +23%")
i3.info("Drama drives 35%")
i4.warning("Mobile contributes 45%")
i5.success("Completion rate +4.6%")