rows = int(input())
matrix = []
row_attack = [-1, -1, -1, 0, 1, 1, 1, 0]
col_attack = [-1, 0, 1, -1, -1, 0, 1, 1]

alive_cells = 0
total_amount = 0

for _ in range(rows):
    matrix.append([int(ch) for ch in input().split(" ")])

bombs = [ch for ch in input().split(" ")]

for charts in bombs:
    row, col = (int(ch) for ch in charts.split(","))

    if 0 <= row < rows and 0 <= col < rows and matrix[row][col] > 0:
        dmg = matrix[row][col]

        for i in range(8):
            current_row = row + row_attack[i]
            current_column = col + col_attack[i]
            if 0 <= current_row < rows and 0 <= current_column < rows and matrix[current_row][current_column] > 0:
                matrix[current_row][current_column] -= dmg

        matrix[row][col] = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] > 0:
            alive_cells += 1
            total_amount += matrix[i][j]

print(f"Alive cells: {alive_cells}")
print(f"Sum: {total_amount}")
for i in range(len(matrix)):
    print(*matrix[i])