def movie_organizer(*args):
    movie_dict = {}
    for chart in args:
        if chart[1] not in movie_dict:
            movie_dict[chart[1]] = []
        movie_dict[chart[1]].append([chart[0]])

    sorted_dict = dict(sorted(movie_dict.items(), key=lambda x: (-len(x[1]), x[0])))

    final_string = ''
    for genre, movies in sorted_dict.items():
        final_string += f"{genre} - {len(movies)}" + '\n'
        for ch in sorted(movies):
            final_string += f"* {''.join(ch)}" + "\n"
    return final_string


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))

