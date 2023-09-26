def sorting_cheeses(**kwargs):
    current_string = ""
    sorted_cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), (x[0])))

    for keys, values in sorted_cheeses:
        current_string += keys + '\n'
        current_string += '\n'.join(str(ch) for ch in sorted(values, reverse=True)) + '\n'
    return current_string


print(sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],)
)