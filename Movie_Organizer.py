

def movie_organizer(*args):
    film_gender = {}

    for movie_name, genre in args:
        if genre not in film_gender:
            film_gender[genre] = []
        film_gender[genre].append(movie_name)


    sorted_result = sorted(film_gender.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ''
    for genre, movie_name in sorted_result:
        sorted_movie = sorted(movie_name)
        result += f"{genre} - {len(sorted_movie)}\n"
        for name in sorted_movie:
            result += f"* {name}\n"
    return result.strip()



print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))


