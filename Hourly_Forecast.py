def forecast(*args):
    location = {}
    for el in args:
        if el[0] not in location:
            location[el[0]] = el[1]
    sorted_result = {k: v for k, v in sorted(location.items(), key=lambda x: (x[1], x[0]))}
    sunny_loc = ''
    rainy_loc = ''
    cloudy_loc = ''
    for key, value in sorted_result.items():
        if value == "Sunny":
            sunny_loc += f"{key} - {value}\n"
        elif value == "Cloudy":
            cloudy_loc += f"{key} - {value}\n"
        elif value == "Rainy":
            rainy_loc += f"{key} - {value}\n"

    return sunny_loc + cloudy_loc + rainy_loc


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
