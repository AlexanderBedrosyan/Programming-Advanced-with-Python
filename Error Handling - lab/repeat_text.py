text = input()
time_of_repeating = input()

try:
    print(text * int(time_of_repeating))
except ValueError:
    print("Variable times must be an integer")