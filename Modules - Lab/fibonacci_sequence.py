from fibonacci_generator.fibonacci_generator import generate_fibonacci


while True:
    sequence = input()
    if sequence == 'Stop':
        break

    sequence = int([ch for ch in sequence.split(' ')][2])
    list_of_fibonacci = generate_fibonacci(sequence)
    print(' '.join(str(ch) for ch in list_of_fibonacci))

    looking_number = int([ch for ch in input().split(' ')][1])

    try:
        index = list_of_fibonacci.index(looking_number)
        print(f"The number - {looking_number} is at index {index}")
    except ValueError:
        print(f"The number {looking_number} is not in the sequence")
