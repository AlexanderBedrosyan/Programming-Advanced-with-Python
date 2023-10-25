from collections import deque


def is_rest(player, rest_players):
    return player in rest_players


moves = deque(ch for ch in input().split(', '))
player_hit_the_wall = []
board = [[ch for ch in input().split(' ')] for _ in range(6)]

command = [ch for ch in input()]

while command:
    player_move = moves.popleft()
    if is_rest(player_move, player_hit_the_wall):
        moves.append(player_move)
        command = [ch for ch in input()]
        player_hit_the_wall.remove(player_move)
        continue

    result_dict = {
        'E': f"{player_move} found the Exit and wins the game!",
        'T': f"{player_move} is out of the game! The winner is {moves[0]}.",
        'W': f"{player_move} hits a wall and needs to rest.",
    }

    row, col = int(command[1]), int(command[4])

    if board[row][col] in 'ET':
        print(result_dict[board[row][col]])
        break
    elif board[row][col] == "W":
        player_hit_the_wall.append(player_move)
        print(result_dict["W"])

    moves.append(player_move)

    command = [ch for ch in input()]
