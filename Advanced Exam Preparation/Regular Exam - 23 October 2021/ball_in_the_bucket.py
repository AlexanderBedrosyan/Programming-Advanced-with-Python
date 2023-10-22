directions = {"left": [0, -1], "right": [0, 1], "down": [1, 0], "up": [-1, 0]}
size = 6
board = [[ch for ch in input().split(' ')]for _ in range(size)]


def is_won_prize(result):
    if 100 <= result <= 199:
        return 'Football'
    if 200 <= result <= 299:
        return 'Teddy Bear'
    if 300 <= result:
        return 'Lego Construction Set'
    return False


def is_valid(row, col, size, board):
    if 0 <= row < size and 0 <= col < size and board[row][col] == 'B':
        return True
    return False


def new_score(col, board, size):
    score = 0
    for current_row in range(0, size):
        if board[current_row][col].isdigit():
            score += int(board[current_row][col])
    return score


total_score = 0


for _ in range(3):
    tuple_points = input().split(', ')
    row = int(tuple_points[0][1:])
    col = int(tuple_points[1][:-1])

    if not is_valid(row, col, size, board):
        continue

    total_score += new_score(col, board, size)
    board[row][col] = '0'

final_result = is_won_prize(total_score)
if not final_result:
    print(f"Sorry! You need {100 - total_score} points more to win a prize.")
else:
    print(f"Good job! You scored {total_score} points, and you've won {final_result}.")