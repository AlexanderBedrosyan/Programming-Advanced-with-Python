import sys
matrix = []

rows, columns = (int(ch) for ch in input().split(" "))

for _ in range(rows):
    matrix.append([int(ch) for ch in input().split(" ")])

max_sum = -sys.maxsize
final_matrix = []

for row in range(rows - 2):
    for cols in range(columns - 2):
        current_matrix = []

        current_matrix.append([matrix[row][cols], matrix[row][cols + 1], matrix[row][cols + 2]])
        current_matrix.append([matrix[row + 1][cols], matrix[row + 1][cols + 1], matrix[row + 1][cols + 2]])
        current_matrix.append([matrix[row + 2][cols], matrix[row + 2][cols + 1], matrix[row + 2][cols + 2]])
        if (sum(current_matrix[0]) + sum(current_matrix[1]) + sum(current_matrix[2])) > max_sum:
            final_matrix = current_matrix
            max_sum = sum(current_matrix[0]) + sum(current_matrix[1]) + sum(current_matrix[2])

print(f"Sum = {max_sum}")
for i in range(len(final_matrix)):
    print(*final_matrix[i])