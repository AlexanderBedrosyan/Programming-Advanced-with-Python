def is_valid(row, rows, col, columns):
    if 0 <= row < rows and 0 <= col < columns:
        return True
    return False


def print_final_result(message, position, board):
    print(message)
    board[position[0]][position[1]] = 'M'
    for line in board:
        print(''.join(line))


rows, columns = [int(ch) for ch in input().split(',')]
directions = {"up": [-1, 0], "down": [1, 0], "right": [0, 1], "left": [0, -1]}
cupboard_area = [[ch for ch in input()]for _ in range(rows)]
mouse_position = [[row, col] for col in range(columns) for row in range(rows) if cupboard_area[row][col] == 'M'][0]
cupboard_area[mouse_position[0]][mouse_position[1]] = "*"
cheese_pieces = sum([1 for col in range(columns) for row in range(rows) if cupboard_area[row][col] == 'C'])


command = input()

while command != 'danger':
    row = mouse_position[0] + directions[command][0]
    col = mouse_position[1] + directions[command][1]

    if not is_valid(row, rows, col, columns):
        print_final_result("No more cheese for tonight!", mouse_position, cupboard_area)
        exit()

    if cupboard_area[row][col] == '@':
        command = input()
        continue

    if cupboard_area[row][col] == 'C':
        cheese_pieces -= 1
        cupboard_area[row][col] = '*'
    elif cupboard_area[row][col] == 'T':
        mouse_position = [row, col]
        print_final_result("Mouse is trapped!", mouse_position, cupboard_area)
        exit()

    mouse_position = [row, col]
    if cheese_pieces == 0:
        print_final_result("Happy mouse! All the cheese is eaten, good night!", mouse_position, cupboard_area)
        exit()
    command = input()

if cheese_pieces > 0:
    print_final_result("Mouse will come back later!", mouse_position, cupboard_area)