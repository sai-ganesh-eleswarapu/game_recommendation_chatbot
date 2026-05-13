import streamlit as st
from components.filters import render_filters


def render_sidebar():

    with st.sidebar:

        st.markdown(
            """
            # 🎮 GameBot AI
            
            ### Intelligent Game Recommendation Assistant
            """
        )

        st.markdown("---")

        filters = render_filters()

        st.markdown("---")

        st.markdown(
            """
            ## ⚡ Features
            
            - AI Recommendations
            - Smart Mood Detection
            - Genre Matching
            - Conversation-Based Suggestions
            - Game Discovery Dashboard
            """
        )

        st.markdown("---")

        st.markdown(
            """
            ## 🧠 Recommendation Engine
            
            Hybrid AI recommendation system using:
            
            - NLP understanding
            - Preference scoring
            - Mood analysis
            - Genre intelligence
            """
        )

    return filters