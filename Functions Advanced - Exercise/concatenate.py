def concatenate(*args, **kwargs):
    new_string = ''
    for ch in args:
        new_string += ch
    for keys, values in kwargs.items():
        if keys in new_string:
            new_string = new_string.replace(keys, values)

    return new_string


print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
