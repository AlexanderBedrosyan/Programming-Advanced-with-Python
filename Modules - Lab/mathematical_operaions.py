from calculator.calculator import calculator

starting_string = input().split(' ')
print(calculator(float(starting_string[0]), starting_string[1], float(starting_string[2])))