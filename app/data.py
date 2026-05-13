import requests

from settings import RAWG_API_KEY


def fetch_game_details(game_name):

    url = "https://api.rawg.io/api/games"

    params = {
        "key": RAWG_API_KEY,
        "search": game_name,
        "page_size": 1
    }

    response = requests.get(url, params=params)

    data = response.json()

    results = data.get("results")

    if not results:
        return None

    game = results[0]

    return {

        "name": game.get("name"),

        "image": game.get("background_image"),

        "description": f"⭐ Rating: {game.get('rating')} | 📅 Released: {game.get('released')}",

        "genre": [
            genre["name"]
            for genre in game.get("genres", [])
        ],

        "platform": [
            platform["platform"]["name"]
            for platform in game.get("platforms", [])
        ],

        "tags": [
            tag["name"]
            for tag in game.get("tags", [])[:5]
        ],

        "link": f"https://rawg.io/games/{game.get('slug')}"
    }