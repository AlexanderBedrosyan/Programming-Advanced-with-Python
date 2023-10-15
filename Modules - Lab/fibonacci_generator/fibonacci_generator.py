def generate_fibonacci(length):
    fibonacci_sequence = []
    a, b = 0, 1

    for _ in range(length):
        fibonacci_sequence.append(a)
        a, b = b, a + b

    return fibonacci_sequence
