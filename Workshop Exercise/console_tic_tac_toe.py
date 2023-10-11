def sign_checker(choose_sign):
    if choose_sign == 'X' or choose_sign == 'O':
        return True
    return False


def board_print(board):
    result = []
    for line in board:
        result.append(f"| {' | '.join(str(ch) for ch in line)} |")
    print('\n'.join(result))


def fill_the_mapper(size):
    current_mapper = {}
    for num in range(1, size * size + 1):
        current_mapper[num] = 0
    all_sizes = []
    for row in range(size):
        for col in range(size):
            all_sizes.append((row, col))
    for key in current_mapper.keys():
        current_mapper[key] = all_sizes[key - 1]
    return current_mapper


def position_checker(current_option, mapper, board):
    if current_option.isdigit() and 1 <= int(current_option) <= 9:
        if board[mapper[int(current_option)][0]][mapper[int(current_option)][1]] is None:
            return True
    return False


def choose_position(player, mapper, board):
    while True:
        current_option = input(f"{player}, choose a free position [1-9]: ")
        if not position_checker(current_option, mapper, board):
            print('You must choose a digit from 1 to 9! Check the free spots below')
            board_print(board)
            continue
        return int(current_option)


def is_winner(board, sign, size):
    rows = [[board[row][col] for col in range(size)] for row in range(size)]
    columns = [[board[row][col] for row in range(size)] for col in range(size)]
    main_diagonal = [board[row][col] for col in range(size) for row in range(size) if row == col]
    secondary_diagonal = [board[row][size - 1 - row] for row in range(size)]
    for i in range(size):
        if rows[i].count(sign) == size:
            return True
        if columns[i].count(sign) == size:
            return True

    if main_diagonal.count(sign) == size:
        return True
    if secondary_diagonal.count(sign) == size:
        return True
    return False


player_one = input('Player one nickname: ')
player_two = input('Player one nickname: ')
sing_player_one = None
sign_player_two = None
size = 3
board = [[None for _ in range(size)] for _ in range(size)]
mapper_board = fill_the_mapper(size)
current_player = 1

while True:
    acceptable_signs = 'XO'
    choose_sign = input(f"{player_one}, whould you like to play with 'X' or 'O'? ").upper()
    if not sign_checker(choose_sign):
        continue

    sing_player_one = choose_sign
    sign_player_two = [ch for ch in acceptable_signs if ch != choose_sign][0]
    break

print('This is the numeration of the board:')
[print(f"| {' | '.join(str(ch + size * i) for ch in range(1, size + 1))} |") for i in range(size)]

while True:
    board_print(board)
    player = None
    sign = None

    if current_player % 2 == 0:
        player = player_two
        sign = sign_player_two
    else:
        player = player_one
        sign = sing_player_one

    position = choose_position(player, mapper_board, board)
    board[mapper_board[position][0]][mapper_board[position][1]] = sign
    if is_winner(board, sign, size):
        print(f"{player} won the game!")
        break
    current_player += 1

