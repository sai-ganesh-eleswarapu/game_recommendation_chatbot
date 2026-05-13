from premium_games import premium_games


def recommend_games(user_input):

    user_input = user_input.lower()

    matched_games = []

    for category, games in premium_games.items():

        category_name = category.replace("_", " ")

        if category_name in user_input:

            matched_games.extend(games)

    if not matched_games:

        matched_games = premium_games["open_world"]

    unique_games = list(dict.fromkeys(matched_games))

    return unique_games[:6]