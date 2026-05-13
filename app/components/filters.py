import streamlit as st


def render_filters():

    st.markdown(
        """
        <div class="filter-title">
            🎯 Smart Filters
        </div>
        """,
        unsafe_allow_html=True
    )

    platform = st.selectbox(
        "Platform",
        ["All", "PC", "Mobile", "PS5", "Xbox"]
    )

    mode = st.selectbox(
        "Mode",
        ["All", "Single", "Multiplayer"]
    )

    genre = st.selectbox(
        "Genre",
        [
            "All",
            "Action",
            "Adventure",
            "RPG",
            "Sports",
            "Strategy",
            "Shooter",
            "Sandbox"
        ]
    )

    mood = st.selectbox(
        "Mood",
        [
            "All",
            "Relaxing",
            "Competitive",
            "Story Rich",
            "Fun",
            "Casual",
            "Creative"
        ]
    )

    return {
        "platform": platform,
        "mode": mode,
        "genre": genre,
        "mood": mood
    }