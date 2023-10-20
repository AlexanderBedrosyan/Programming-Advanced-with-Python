from collections import deque
from math import ceil


def is_inside(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


def is_winner(result, current_player):
    return result[current_player] <= 0


def double_or_triple_result(row, col, darts_board, size, double_or_triple):
    dict_regarding_double_or_triple = {
        'D': 2,
        'T': 3,
    }
    result = 0
    position = [0, size - 1]
    for new_row in position:
        result += int(darts_board[new_row][col])
    for new_col in position:
        result += int(darts_board[row][new_col])
    return result * dict_regarding_double_or_triple[double_or_triple]


size = 7
directions = {"up": [-1, 0], "down": [1, 0], "right": [0, 1], "left": [0, -1]}
players = deque(ch for ch in input().split(', '))
player_result = {player: 501 for player in players}
darts = [[ch for ch in input().split(' ')] for _ in range(size)]
counter = 0

while True:
    counter += 1
    current_player = players.popleft()
    command = input().split(', ')
    row, col = int(command[0][1:]), int(command[1][:-1])

    if not is_inside(row, col, size):
        players.append(current_player)
        continue

    if darts[row][col].isdigit():
        player_result[current_player] -= int(darts[row][col])
    elif darts[row][col] == 'D':
        player_result[current_player] -= double_or_triple_result(row, col, darts, size, 'D')
    elif darts[row][col] == 'T':
        player_result[current_player] -= double_or_triple_result(row, col, darts, size, 'T')
    elif darts[row][col] == 'B':
        print(f"{current_player} won the game with {ceil(counter / 2)} throws!")
        break

    if is_winner(player_result, current_player):
        print(f"{current_player} won the game with {ceil(counter / 2)} throws!")
        break

    players.append(current_player)
