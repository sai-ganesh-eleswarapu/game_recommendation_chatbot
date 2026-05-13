import streamlit as st


def render_game_cards(games):

    if not games:
        st.warning("No games found.")
        return

    cols = st.columns(3)

    for index, game in enumerate(games):

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

            badge_text = (
                f"🎯 {', '.join(game['genre'])} | "
                f"🖥️ {', '.join(game['platform'])} | "
                f"🎮 {game['mode']}"
            )

            st.caption(badge_text)

            tags = " • ".join(game["tags"])

            st.markdown(
                f"""
                <div style="
                    margin-top:10px;
                    margin-bottom:15px;
                    color:#9ca3af;
                    font-size:14px;
                ">
                    {tags}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.link_button(
                "🔗 View Game",
                game["link"],
                use_container_width=True
            )

            st.markdown("---")