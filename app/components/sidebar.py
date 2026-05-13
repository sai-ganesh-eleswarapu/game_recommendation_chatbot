import streamlit as st
from components.filters import render_filters


def render_sidebar():

    with st.sidebar:

        st.markdown(
            """
            <div class="sidebar-container">

                <div class="sidebar-logo">
                    🎮
                </div>

                <div class="sidebar-title">
                    GameBot AI
                </div>

                <div class="sidebar-subtitle">
                    Intelligent Game Recommendation Assistant
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("---")

        filters = render_filters()

        st.markdown("---")

        st.markdown(
            """
            <div class="sidebar-section">

                <div class="sidebar-heading">
                    ⚡ Features
                </div>

                <ul class="feature-list">
                    <li>AI Recommendations</li>
                    <li>Smart Mood Detection</li>
                    <li>Genre Matching</li>
                    <li>Conversation-Based Suggestions</li>
                    <li>Game Discovery Dashboard</li>
                </ul>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("---")

        st.markdown(
            """
            <div class="sidebar-section">

                <div class="sidebar-heading">
                    🧠 Recommendation Engine
                </div>

                <div class="sidebar-text">
                    Hybrid AI recommendation system using:
                    <br><br>
                    • NLP understanding
                    <br>
                    • Preference scoring
                    <br>
                    • Mood analysis
                    <br>
                    • Genre intelligence
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    return filters