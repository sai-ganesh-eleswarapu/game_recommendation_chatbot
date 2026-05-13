import streamlit as st

from styles import custom_css
from recommender import recommend_games
from chatbot import generate_ai_response

from components.sidebar import render_sidebar
from components.chat import (
    render_user_message,
    render_bot_message
)
from components.cards import render_game_cards


def render_ui():

    st.set_page_config(
        page_title="Game Recommendation Dashboard",
        layout="wide"
    )

    st.markdown(custom_css, unsafe_allow_html=True)

    filters = render_sidebar()

    st.markdown(
        """
        <div class="main-title">
            🎮 Game Recommendation Dashboard
        </div>

        <div class="subtitle">
            Discover games based on your mood and preferences
        </div>
        """,
        unsafe_allow_html=True
    )

    user_input = st.chat_input(
        "Type your gaming preferences..."
    )

    if user_input:

        render_user_message(user_input)

        recommended_games = recommend_games(user_input)

        if recommended_games:

            ai_response = generate_ai_response(
                user_input,
                recommended_games
            )

            render_bot_message(ai_response)

            st.markdown(
                """
                <div style="
                    margin-top:30px;
                    margin-bottom:20px;
                    font-size:28px;
                    font-weight:700;
                ">
                    🔥 Recommended Games
                </div>
                """,
                unsafe_allow_html=True
            )

            render_game_cards(recommended_games)

        else:

            render_bot_message(
                "Sorry, I couldn't find matching games."
            )