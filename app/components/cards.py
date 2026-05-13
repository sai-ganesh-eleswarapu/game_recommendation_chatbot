import streamlit as st


def render_game_cards(games):

    if not games:
        st.warning("No games found.")
        return

    cols = st.columns(3)

    for index, game in enumerate(games):

        with cols[index % 3]:

            st.markdown(
                f"""
                <div class="game-card">

                    <img src="{game['image']}" class="game-image">

                    <div class="game-content">

                        <div class="game-header">
                            <div class="game-title">
                                🎮 {game['name']}
                            </div>
                        </div>

                        <div class="game-description">
                            {game['description']}
                        </div>

                        <div class="badge-container">
                            <span class="badge genre-badge">
                                {game['genre'][0]}
                            </span>

                            <span class="badge platform-badge">
                                {game['platform'][0]}
                            </span>

                            <span class="badge mode-badge">
                                {game['mode']}
                            </span>
                        </div>

                        <div class="tags-container">
                            {" ".join([f'<span class="tag">{tag}</span>' for tag in game['tags']])}
                        </div>

                        <a href="{game['link']}" target="_blank">
                            <button class="game-button">
                                🔗 View Game
                            </button>
                        </a>

                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )