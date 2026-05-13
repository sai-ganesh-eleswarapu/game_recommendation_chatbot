from app.data import games_data


def recommend_games(user_input):
    user_input = user_input.lower()

    recommendations = []

    for game in games_data:
        score = 0

        for genre in game["genre"]:
            if genre.lower() in user_input:
                score += 5

        for mood in game["mood"]:
            if mood.lower() in user_input:
                score += 4

        for tag in game["tags"]:
            if tag.lower() in user_input:
                score += 3

        if "friends" in user_input or "multiplayer" in user_input:
            if game["mode"] == "Multiplayer":
                score += 5

        if "story" in user_input:
            if "Story Rich" in game["tags"]:
                score += 5

        if "mobile" in user_input:
            if "Mobile" in game["platform"]:
                score += 5

        if "pc" in user_input:
            if "PC" in game["platform"]:
                score += 5

        if score > 0:
            recommendations.append((score, game))

    recommendations.sort(reverse=True, key=lambda x: x[0])

    return [game for score, game in recommendations[:6]]