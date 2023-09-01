def is_valid(row1, col1, row2, col2, rows, columns):
    if 0 <= row1 < rows and 0 <= row2 < rows and 0 <= col1 < columns and 0 <= col2 < columns:
        return True
    else:
        return False


matrix = []
rows, columns = (int(ch) for ch in input().split(" "))

for _ in range(rows):
    matrix.append([ch for ch in input().split(" ")])

while True:
    command = input().split(" ")

    if command[0] == "END":
        break
    elif len(command) != 5:
        print("Invalid input!")
        continue

    if command[0] == "swap" and len(command) == 5:
        row1, col1, row2, col2 = int(command[1]), int(command[2]), int(command[3]), int(command[4])

    if is_valid(row1, col1, row2, col2, rows, columns):
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        for i in range(len(matrix)):
            print(*matrix[i])
    else:
        print("Invalid input!")