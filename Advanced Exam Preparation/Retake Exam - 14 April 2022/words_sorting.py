def words_sorting(*args):
    main_dictionary = {}

    for word in args:
        if word in main_dictionary:
            continue
        main_dictionary[word] = 0
        for letter in word:
            main_dictionary[word] += ord(letter)

    result = []
    if sum(main_dictionary.values()) == 0:
        pass
    elif sum(main_dictionary.values()) % 2 == 0:
        main_dictionary = dict(sorted(main_dictionary.items(), key=lambda x: x[0]))
    else:
        main_dictionary = dict(sorted(main_dictionary.items(), key=lambda x: -x[1]))

    for key, value in main_dictionary.items():
        result.append(f"{key} - {value}")
    return '\n'.join(result)
