from collections import deque


def check_diagonals(position, board, player):
    row, col = position
    if player == 'white':
        if col > 0 and row > 0 and board[row - 1][col - 1] == 'b':
            return [row - 1, col - 1]
        if col < 7 and row > 0 and board[row - 1][col + 1] == 'b':
            return [row - 1, col + 1]
    if player == 'black':
        if col > 0 and row < 7 and board[row + 1][col - 1] == 'w':
            return [row + 1, col - 1]
        if col < 7 and row < 7 and board[row + 1][col + 1] == 'w':
            return [row + 1, col + 1]
    return False


size = 8
players = deque(['white', 'black'])
col_dict = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
row_dict = {0: '8', 1: '7', 2: '6', 3: '5', 4: '4', 5: '3', 6: '2', 7: '1'}
chess_board = [[ch for ch in input().split(' ')] for _ in range(size)]

player_positions = {
    'white': [[row, col] for col in range(size) for row in range(size) if chess_board[row][col] == 'w'][0],
    'black': [[row, col] for col in range(size) for row in range(size) if chess_board[row][col] == 'b'][0]
}

while True:
    current_player = players.popleft()
    result = check_diagonals(player_positions[current_player], chess_board, current_player)
    row, col = 0, 0

    if result:
        row, col = result
        winner = current_player[0].upper() + current_player[1:]
        print(f"Game over! {winner} win, capture on {col_dict[col]}{row_dict[row]}.")
        break

    if current_player == 'white':
        row = player_positions[current_player][0] - 1
        col = player_positions[current_player][1]
        if row == 0:
            winner = current_player[0].upper() + current_player[1:]
            print(f"Game over! {winner} pawn is promoted to a queen at {col_dict[col]}{row_dict[row]}.")
            break
    elif current_player == 'black':
        row = player_positions[current_player][0] + 1
        col = player_positions[current_player][1]
        if row == 7:
            winner = current_player[0].upper() + current_player[1:]
            print(f"Game over! {winner} pawn is promoted to a queen at {col_dict[col]}{row_dict[row]}.")
            break

    chess_board[player_positions[current_player][0]][player_positions[current_player][1]] = '-'
    chess_board[row][col] = current_player[0]
    player_positions[current_player] = [row, col]
    players.append(current_player)
