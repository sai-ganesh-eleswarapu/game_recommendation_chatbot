import google.generativeai as genai
from config.settings import GEMINI_API_KEY


genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


def generate_ai_response(user_input, recommended_games):
    game_names = ", ".join([game["name"] for game in recommended_games])

    prompt = f"""
    User input: {user_input}

    Recommended games: {game_names}

    Act like a professional gaming recommendation assistant.

    Explain naturally and conversationally why these games match the user's preferences.

    Keep response concise, friendly, and modern.
    """

    response = model.generate_content(prompt)

    return response.text