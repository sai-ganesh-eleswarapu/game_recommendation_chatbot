
from statistics import mode


def get_ai_recommendation(genre, platform, mode):
    if genre == "Action":
        games = ["Call of Duty", "GTA V", "Apex Legends"]
    elif genre == "Adventure":
        games = ["Zelda", "Uncharted", "Tomb Raider"]
    elif genre == "Sports":
        games = ["FIFA", "NBA 2K", "WWE 2K"]
    else:
        games = ["Civilization VI", "Age of Empires", "Clash of Clans"]

    response = "🎮 Here are your recommendations:\n\n"

    for i, game in enumerate(games, 1):
        response += f"{i}. {game} - Perfect for {genre} lovers on {platform} ({mode}) mode.\n"

    return response