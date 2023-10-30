def validator(board, current_row, current_col):
    if 0 <= current_row < len(board) and 0 <= current_col < len(board[0]):
        return True
    return False


def result_of_box(board, row, col, directions):
    amount_of_the_box = 0
    for value in directions.values():
        current_row = row + value[0]
        current_col = col + value[1]
        if not validator(board, current_row, current_col):
            continue
        if board[current_row][current_col] == "*":
            amount_of_the_box += 1
    return amount_of_the_box


directions = {
    "left": [0, -1],
    "right": [0, 1],
    "down": [1, 0],
    "up": [-1, 0],
    "top_left_diagonal": [-1, -1],
    "top_right_diagonal": [-1, 1],
    "bottom_right_diagonal": [1, 1],
    "bottom_left_diagonal": [1, -1],
}

size = int(input())
num = int(input())

board = [[None for _ in range(size)] for _ in range(size)]

for _ in range(num):
    command = input()
    command = command.split(', ')
    row = int(command[0][1:])
    col = int(command[1][:-1])

    if validator(board, row, col):
        board[row][col] = '*'


for row in range(size):
    for col in range(size):
        if board[row][col] == '*':
            continue
        board[row][col] = result_of_box(board, row, col, directions)

[print(' '.join(str(ch) for ch in line)) for line in board]
