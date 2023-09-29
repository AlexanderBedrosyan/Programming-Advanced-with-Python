def grocery_store(**kwargs):
    result = ''
    for key, values in sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])):
        result += key + ": " + f'{values}' + '\n'
    return result


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
