import streamlit as st


def render_user_message(message):

    with st.chat_message("user"):
        st.write(message)


def render_bot_message(message):

    with st.chat_message("assistant"):
        st.write(message)