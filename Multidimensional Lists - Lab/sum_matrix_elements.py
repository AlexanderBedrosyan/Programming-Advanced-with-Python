row, column = (int(ch) for ch in input().split(", "))
matrix = []
result = 0

for _ in range(row):
    matrix.append([int(ch) for ch in input().split(", ")])

for i in range(len(matrix)):
    result += sum(matrix[i])

print(result)
print(matrix)
