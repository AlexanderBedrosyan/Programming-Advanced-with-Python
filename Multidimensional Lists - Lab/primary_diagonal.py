matrix = []
rows = int(input())

for _ in range(rows):
    matrix.append([int(ch) for ch in input().split(" ")])

result = 0

for row in range(rows):
    for column in range(len(matrix[row])):
        if column == row:
            result += matrix[row][column]

print(result)