def is_valid(row, col):
    if 0 <= row < 8 and 0 <= col < 8:
        return True
    return False


def is_capture_the_king(chess_board, position, direction):
    while True:
        row = position[0] + direction[0]
        col = position[1] + direction[1]
        if not is_valid(row, col):
            return False
        if chess_board[row][col] == 'Q':
            return False
        if chess_board[row][col] == 'K':
            return True
        position = [row, col]


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

chess_board = [[ch for ch in input().split(' ')] for _ in range(8)]
queens_position = []
queens_who_capture_the_king = []

for row in range(8):
    for col in range(8):
        if chess_board[row][col] == 'Q':
            queens_position.append([row, col])

for position in queens_position:
    for direction in directions.values():
        result = is_capture_the_king(chess_board, position, direction)
        if not result:
            continue
        queens_who_capture_the_king.append(position)

if queens_who_capture_the_king:
    for line in queens_who_capture_the_king:
        print(f"[{', '.join(str(ch) for ch in line)}]")
else:
    print('The king is safe!')