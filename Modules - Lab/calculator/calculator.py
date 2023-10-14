def calculator(num1, sign, num2):
    calculations = {
        '/': num1 / num2,
        '*': num1 * num2,
        '-': num1 - num2,
        '+': num1 + num2,
        '^': num1 ** num2,
    }
    return f"{calculations[sign]:.2f}"