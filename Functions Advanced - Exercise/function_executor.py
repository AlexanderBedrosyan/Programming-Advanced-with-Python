def func_executor(*args):
    current_dict = {}
    needed_string = ''
    for ch in args:
        current_dict[ch[0].__name__] = ch[0](*ch[1])

    for keys, values in current_dict.items():
        needed_string += f'{keys} ' + '-' + f' {values}' + '\n'

    return needed_string


def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result


def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result


print(func_executor((make_upper, ("Python", "softUni")), (make_lower, ("PyThOn",)),))
