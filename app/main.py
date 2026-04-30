import streamlit as st
from app.chatbot import get_ai_recommendation

st.title("🎮 Game Recommendation Chatbot")

st.write("Choose your preferences and get game recommendations instantly 🎯")

genre = st.selectbox("Select Genre", ["Action", "Adventure", "Sports", "Strategy"])
platform = st.selectbox("Select Platform", ["PC", "Mobile"])
mode = st.selectbox("Select Mode", ["Single", "Multiplayer"])

if st.button("Recommend"):
    with st.spinner("Finding best games for you..."):
        result = get_ai_recommendation(genre, platform, mode)
        st.success("Here are your recommendations:")
        st.markdown(result)