rows = int(input())
matrix = []

for _ in range(rows):
    matrix.append([int(ch) for ch in input().split(" ")])

column = len(matrix[0])

while True:
    command = input()

    if command == "END":
        break

    current_command, row, col, value = command.split(" ")

    if 0 <= int(row) < rows and 0 <= int(col) < column:
        if current_command == "Add":
            matrix[int(row)][int(col)] += int(value)
        elif current_command == "Subtract":
            matrix[int(row)][int(col)] -= int(value)
    else:
        print("Invalid coordinates")

for i in range(len(matrix)):
    print(*matrix[i])