def numbers_searching(*args):
    missing_numbers = []
    all_numbers = []
    repeating_numbers = []
    max_number = max(args)
    min_number = min(args)
    for num in range(min_number, max_number + 1):
        if num not in args:
            missing_numbers.append(num)
            continue
        all_numbers.append(num)
    for element in all_numbers:
        if args.count(element) > 1:
            repeating_numbers.append(element)
    missing_numbers.append(repeating_numbers)
    return missing_numbers


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))