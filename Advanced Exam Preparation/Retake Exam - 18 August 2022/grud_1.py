def matrix_creation():
    current_matrix = []
    for _ in range(6):
        current_matrix.append([ch for ch in input().split(" ")])
    return current_matrix


def create(matrix, directions, move, value, current_position):
    row, col = (current_position[0] + directions[move][0]), (current_position[1] + directions[move][1])
    new_position = [row, col]
    if matrix[row][col] == ".":
        matrix[row][col] = value
    return matrix, new_position


def update(matrix, directions, move, value, current_position):
    row, col = (current_position[0] + directions[move][0]), (current_position[1] + directions[move][1])
    new_position = [row, col]
    if matrix[row][col] != ".":
        matrix[row][col] = value
    return matrix, new_position


def delete(matrix, directions, move, current_position):
    row, col = (current_position[0] + directions[move][0]), (current_position[1] + directions[move][1])
    new_position = [row, col]
    if matrix[row][col] != ".":
        matrix[row][col] = "."
    return matrix, new_position


def read(matrix, directions, move, current_position):
    row, col = (current_position[0] + directions[move][0]), (current_position[1] + directions[move][1])
    new_position = [row, col]
    if matrix[row][col] != ".":
        print(matrix[row][col])
    return matrix, new_position


matrix = matrix_creation()
directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
position = input()
position = [int(position[1]), int(position[4])]

command = input()

while command != "Stop":
    current_command = command.split(", ")

    if current_command[0] == "Create":
        move, value = current_command[1], current_command[2]
        matrix, position = create(matrix, directions, move, value, position)
    elif current_command[0] == "Update":
        move, value = current_command[1], current_command[2]
        matrix, position = update(matrix, directions, move, value, position)
    elif current_command[0] == "Delete":
        move = current_command[1]
        matrix, position = delete(matrix, directions, move, position)
    elif current_command[0] == "Read":
        move = current_command[1]
        matrix, position = read(matrix, directions, move, position)

    command = input()

[print(*ch) for ch in matrix]
