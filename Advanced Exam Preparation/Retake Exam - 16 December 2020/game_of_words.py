def validator(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


directions = {
    "left": [0, -1],
    "right": [0, 1],
    "down": [1, 0],
    "up": [-1, 0],
}

initial_string = input()
size = int(input())

words_board = [[element for element in input()] for _ in range(size)]
player_position = [[row, col] for col in range(size) for row in range(size) if words_board[row][col] == 'P'][0]
words_board[player_position[0]][player_position[1]] = '-'

num = int(input())

for _ in range(num):
    command = input()
    row = directions[command][0] + player_position[0]
    col = directions[command][1] + player_position[1]

    if not validator(row, col, size):
        if initial_string:
            initial_string = initial_string[:-1]
        continue

    if words_board[row][col] != '-':
        initial_string += words_board[row][col]
        words_board[row][col] = '-'

    player_position = [row, col]

words_board[player_position[0]][player_position[1]] = 'P'
print(initial_string)
for line in words_board:
    print(''.join(line))
