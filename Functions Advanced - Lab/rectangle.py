def area(*args):
    return args[0] * args[1]


def perimeter(*args):
    return 2 * args[0] + 2 * args[1]


def rectangle(*args):
    check = True
    numbers = []
    for ch in args:
        if type(ch) == int:
            numbers.append(ch)
            continue
        else:
            check = False
            return "Enter valid values!"

    if check:
        return f'Rectangle area: {area(numbers[0], numbers[1])}\n' \
               f'Rectangle perimeter: {perimeter(numbers[0], numbers[1])}'


print(rectangle('2', 10))