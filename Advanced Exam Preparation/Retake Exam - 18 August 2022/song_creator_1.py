def add_songs(*args):
    author_lyrics = {}
    for elements in args:
        name = elements[0]
        lyrics = elements[1]
        if name not in author_lyrics:
            author_lyrics[name] = []
        if len(lyrics) > 0:
            for ch in lyrics:
                author_lyrics[name].append(ch)
    final_result = []
    for name, lyrics in author_lyrics.items():
        final_result.append(f"- {name}")
        for text in lyrics:
            final_result.append(text)
    return '\n'.join(final_result)


print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))
