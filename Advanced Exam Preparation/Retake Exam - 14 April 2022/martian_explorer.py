def correct_coordinates(row, col):
    if row >= 6:
        row = 0
    if row < 0:
        row = 5
    if col >= 6:
        col = 0
    if col < 0:
        col = 5
    return row, col


directions = {
    "left": [0, -1],
    "right": [0, 1],
    "down": [1, 0],
    "up": [-1, 0],
}

board = [[ch for ch in input().split(' ')]for _ in range(6)]
needed_elements = ['W', 'M', 'C']
rover_position = [[row, col] for col in range(6) for row in range(6) if board[row][col] == 'E'][0]

commands = input().split(', ')

for command in commands:
    row = rover_position[0] + directions[command][0]
    col = rover_position[1] + directions[command][1]
    row, col = correct_coordinates(row, col)

    message_dict = {
        'W': f"Water deposit found at ({row}, {col})",
        'C': f"Concrete deposit found at ({row}, {col})",
        'M': f"Metal deposit found at ({row}, {col})"
    }

    if board[row][col] == 'R':
        print(f"Rover got broken at ({row}, {col})")
        break
    elif board[row][col] in 'WCM':
        print(message_dict[board[row][col]])
        if board[row][col] in needed_elements:
            needed_elements.remove(board[row][col])

    rover_position = [row, col]

if not needed_elements:
    print("Area suitable to start the colony.")
else:
    print(f"Area not suitable to start the colony.")