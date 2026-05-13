import google.generativeai as genai

from settings import GEMINI_API_KEY


genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash-8b")

def generate_ai_response(user_input, games):

    game_names = ", ".join([game["name"] for game in games])

    return f"""
    Based on your interest, these games match your preferences:
    
    {game_names}
    
    These games align with your requested genre and gameplay style.
    """

    try:

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        return f"⚠️ AI Error: {str(e)}"