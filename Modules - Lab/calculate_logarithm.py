from math import log

num = int(input())
num2 = input()
try:
    print(f"{log(num, int(num2)):.2f}")
except ValueError:
    print(f"{log(num):.2f}")
