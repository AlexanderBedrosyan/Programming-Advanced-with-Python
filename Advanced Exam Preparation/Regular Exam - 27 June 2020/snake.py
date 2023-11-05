board = []
size = int(input())
snake_position = []
burrow_positions = []
food = 0
directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}

for row in range(size):
    line = [ch for ch in input()]
    board.append(line)
    for col in range(len(line)):
        if line[col] == "S":
            snake_position.append([row, col])
            board[snake_position[0][0]][snake_position[0][1]] = "."
        if line[col] == "B":
            burrow_positions.append([row, col])

while True:
    command = input()

    current_row = 0
    current_col = 0

    for key, value in directions.items():
        if key == command:
            current_row += snake_position[0][0] + value[0]
            current_col += snake_position[0][1] + value[1]
            break

    if 0 <= current_row < size and 0 <= current_col < size:
        snake_position = []
        if board[current_row][current_col] == "B":
            board[current_row][current_col] = "."
            ind = burrow_positions.index([current_row, current_col])
            del burrow_positions[ind]
            snake_position.append([burrow_positions[0][0], burrow_positions[0][1]])
            board[snake_position[0][0]][snake_position[0][1]] = "."
        elif board[current_row][current_col] == "*":
            food += 1
            if food == 10:
                board[current_row][current_col] = "S"
                break
            snake_position.append([current_row, current_col])
            board[snake_position[0][0]][snake_position[0][1]] = "."
        else:
            snake_position.append([current_row, current_col])
            board[snake_position[0][0]][snake_position[0][1]] = "."
    else:
        board[snake_position[0][0]][snake_position[0][1]] = "."
        break

if food < 10:
    print(f"Game over!\nFood eaten: {food}")
    for ch in board:
        print(''.join(ch))
else:
    print(f"You won! You fed the snake.\nFood eaten: {food}")
    for ch in board:
        print(''.join(ch))
