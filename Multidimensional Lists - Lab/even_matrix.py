matrix = []
num = int(input())

for _ in range(num):
    matrix.append([int(ch) for ch in input().split(", ") if int(ch) % 2 == 0])

print(matrix)