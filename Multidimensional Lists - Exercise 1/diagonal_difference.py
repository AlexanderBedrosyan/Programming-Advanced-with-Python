matrix = []
rows = int(input())

for _ in range(rows):
    matrix.append([int(ch) for ch in input().split(" ")])

primary_diagonal = []
secondary_diagonal = []

for i in range(rows):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][rows - 1 - i])

print(f"{abs(sum(primary_diagonal) - sum(secondary_diagonal))}")
