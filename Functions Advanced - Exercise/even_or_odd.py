def even_odd(*args):
    result = []
    current_list = []
    for ch in args:
        current_list.append(ch)

    x = current_list.pop()

    for ch in current_list:
        if x == "even":
            if ch % 2 == 0:
                result.append(ch)
        else:
            if ch % 2 != 0:
                result.append(ch)
    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
