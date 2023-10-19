from math import floor


def find_correct_step(step, size):
    if step < 0:
        step = size - 1
    if step > (size - 1):
        step = 0
    return step


def steps_validator(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


def is_valid_command(curr_command, curr_directions):
    return curr_command in directions


directions = {
    "left": [0, -1],
    "right": [0, 1],
    "down": [1, 0],
    "up": [-1, 0],
}

size = int(input())
board = [[ch for ch in input().split(' ')] for _ in range(size)]
player_position = [[row, col] for col in range(size) for row in range(size) if board[row][col] == 'P'][0]
all_steps = []
all_steps.append(player_position)
board[player_position[0]][player_position[1]] = '0'
collector = 0

while collector < 100:
    command = input()

    if not is_valid_command(command, directions):
        continue

    row = directions[command][0] + player_position[0]
    col = directions[command][1] + player_position[1]

    if not steps_validator(row, col, size):
        row = find_correct_step(row, size)
        col = find_correct_step(col, size)

    if board[row][col].isdigit():
        collector += int(board[row][col])
        board[row][col] = '0'
    if board[row][col] == 'X':
        print(f"Game over! You've collected {floor(collector / 2)} coins.\nYour path:")
        all_steps.append([row, col])
        [print(position) for position in all_steps]
        exit()

    player_position = [row, col]
    all_steps.append(player_position)

print(f"You won! You've collected {collector} coins.\nYour path:")
[print(position) for position in all_steps]