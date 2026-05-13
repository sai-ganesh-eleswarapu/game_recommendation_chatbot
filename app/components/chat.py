import streamlit as st


def render_user_message(message):

    st.markdown(
        f"""
        <div class="user-chat-container">

            <div class="user-chat-bubble">
                <div class="chat-role">
                    🧑 You
                </div>

                <div class="chat-message">
                    {message}
                </div>
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


def render_bot_message(message):

    st.markdown(
        f"""
        <div class="bot-chat-container">

            <div class="bot-chat-bubble">

                <div class="chat-role">
                    🤖 GameBot
                </div>

                <div class="chat-message">
                    {message}
                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )