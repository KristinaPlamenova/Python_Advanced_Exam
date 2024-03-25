def team_lineup(*args):
    country_count = {}
    for arg in args:
        player_name, country_name = arg
        if country_name not in country_count:
            country_count[country_name] = []
        country_count[country_name].append(player_name)

    sorted_result = dict(sorted(country_count.items(), key=lambda x: (-len(x[1]), x[0])))
    result = ' '

    for key, value in sorted_result.items():
        result += f'{key}:\n'







print(team_lineup(
    ("Harry Kane", "England"),
    ("Manuel Neuer", "Germany"),
    ("Raheem Sterling", "England"),
    ("Toni Kroos", "Germany"),
    ("Cristiano Ronaldo", "Portugal"),
    ("Thomas Muller", "Germany")))

