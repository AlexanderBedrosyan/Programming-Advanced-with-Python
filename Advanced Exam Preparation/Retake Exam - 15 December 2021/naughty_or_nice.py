def naughty_or_nice_list(*args, **kwargs):
    kids_list = args[0]
    commands = args[1:]
    naughty_or_nice_dict = kwargs
    final_result = {
        'Nice': [],
        'Naughty': [],
        'Not found:': []
    }
    for curr_command in commands:
        curr_command = curr_command.split('-')
        number_needed = int(curr_command[0])
        type_of_kid = curr_command[1]
        index = []
        for i in range(len(kids_list)):
            if int(kids_list[i][0]) == number_needed:
                index.append(i)

        if len(index) == 1:
            position = index[0]
            final_result[type_of_kid].append(kids_list[position][1])
            kids_list.pop(position)

    for name, kid_type in naughty_or_nice_dict.items():
        index = []
        for i in range(len(kids_list)):
            if kids_list[i][1] == name:
                index.append(i)

        if len(index) == 1:
            position = index[0]
            final_result[kid_type].append(kids_list[position][1])
            kids_list.pop(position)

    if kids_list:
        for information in kids_list:
            final_result['Not found:'].append(information[1])

    return_result = []
    for key, value in final_result.items():
        if len(value) == 0:
            continue
        if key != 'Not found:':
            return_result.append(f"{key}: {', '.join(value)}")
        else:
            return_result.append(f"{key} {', '.join(value)}")
    return '\n'.join(return_result)


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))


print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
