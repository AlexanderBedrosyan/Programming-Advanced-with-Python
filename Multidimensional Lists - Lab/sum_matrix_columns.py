matrix = []
rows, columns = (int(ch) for ch in input().split(", "))

for _ in range(rows):
    matrix.append([int(ch) for ch in input().split(" ")])

for column in range(columns):
    result = 0
    for row in range(len(matrix)):
        result += matrix[row][column]
    print(result)
