import streamlit as st

from recommender import recommend_games
from data import fetch_game_details


def render_ui():

    st.set_page_config(
        page_title="Game Recommendation Dashboard",
        page_icon="🎮",
        layout="wide"
    )

    st.markdown(
        """
        <style>

        .stApp {
            background-color: #050816;
            color: white;
        }

        .main-title {
            font-size: 56px;
            font-weight: 800;
            color: white;
            margin-bottom: 8px;
        }

        .subtitle {
            font-size: 18px;
            color: #9ca3af;
            margin-bottom: 40px;
        }

        .stChatInputContainer {
            border: 1px solid #1f2937;
            border-radius: 14px;
            background-color: #111827;
        }

        div[data-testid="stVerticalBlock"] > div:has(div.stImage) {
            background: linear-gradient(
                145deg,
                #111827,
                #0f172a
            );
            padding: 18px;
            border-radius: 18px;
            border: 1px solid #1f2937;
            margin-bottom: 20px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="main-title">
            🎮 Game Recommendation Dashboard
        </div>

        <div class="subtitle">
            Discover the best games based on your mood, genre, platform and play style
        </div>
        """,
        unsafe_allow_html=True
    )

    user_input = st.chat_input(
        "Type your gaming preferences..."
    )

    if user_input:

        st.chat_message("user").write(user_input)

        recommended_games = recommend_games(user_input)

        st.chat_message("assistant").write(
            "🔥 Here are the best recommendations for you"
        )

        st.write("")

        cols = st.columns(3)

        for index, game_name in enumerate(recommended_games):

            game = fetch_game_details(game_name)

            if not game:
                continue

            with cols[index % 3]:

                st.image(
                    game["image"],
                    use_container_width=True
                )

                st.markdown(
                    f"""
                    ### 🎮 {game['name']}
                    """
                )

                st.write(game["description"])

                st.caption(
                    f"🎯 {' • '.join(game['genre'][:3])}"
                )

                st.caption(
                    f"🖥️ {' • '.join(game['platform'][:3])}"
                )

                st.caption(
                    f"🏷️ {' • '.join(game['tags'][:4])}"
                )

                st.link_button(
                    "🎮 View Game",
                    game["link"],
                    use_container_width=True
                )

                st.divider()