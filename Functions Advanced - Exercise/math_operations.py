def math_operations(*args, **kwargs):
    count = 0
    final_result = ''
    for digit in args:
        count += 1
        if count == 1:
            kwargs["a"] += digit
        elif count == 2:
            kwargs["s"] -= digit
        elif count == 3:
            if digit == 0:
                continue
            else:
                kwargs["d"] /= digit
        elif count == 4:
            kwargs["m"] *= digit
            count = 0

    for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], x[0])):
        final_result += f"{key}" + ": " + f"{value:.1f}" + "\n"

    return final_result


print(math_operations(6.0, a=0, s=0, d=5, m=0))
