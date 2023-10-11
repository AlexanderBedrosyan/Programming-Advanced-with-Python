def while_working(board):
    """
    This function checking if the main while loop should continue. It's passing if there is at least one ZERO cell.
    :param board: the matrix of the game
    :return: False or True
    """
    for line in board:
        if 0 in line:
            return True
    return False


def is_integer(current_column, columns):
    """
    This is the first condition of the player choice. Every player should choice only integer numbers for next moves.
    :param current_column: Marked option
    :param columns: Number of columns. This used only for the print
    :return: True or False
    """
    try:
        current_column = int(current_column)
    except ValueError:
        print(f'You should choose a number from 1 to {columns}')
        return False
    return True


def valid_column(current_column, columns):
    """
    Second condition of the player option. Player should mark only numbers from 1 to column count.
    :param current_column: Player choice
    :param columns: Amount of columns
    :return: True or False
    """
    if 0 < int(current_column) <= columns:
        return True
    print(f'You should choose a number from 1 to {columns}')
    return False


def is_free_space(board, current_column):
    """
    This condition is used for checking if in the pipe there is free space on top of the pipe to put the player number there.
    :param board: matrix of the game
    :param current_column: player choice
    :return: row if there is a free place, None if the pipe is full
    """
    rows = len(board)
    for row in range(rows - 1, - 1, - 1):
        if board[row][int(current_column) - 1] == 0:
            return row
    print('There is no free space. Please choose another column.')
    return None


def players_option():
    """
    This is where every player chose where it wants to put his numbers.
    :return: if all conditions are True, return the decision of each player.
    """
    player = input('Players option (not more than 5):')
    try:
        player = int(player)
    except ValueError:
        raise f"Start the game again and choose an option from 1-5!"
    if 0 >= int(player) or int(player) > 5:
        raise ValueError("Players should be number between 0 and 5")
    return player


def choose_column(columns, player, board):
    while True:
        current_column = input(f"Player {player}, please choose a column:")
        if not is_integer(current_column, columns):
            continue
        if not valid_column(current_column, columns):
            continue
        row = is_free_space(board, current_column)
        if not isinstance(row, int):
            continue
        return int(current_column), row


def in_line(board, row, starting_columns, columns):
    for col in range(starting_columns - 4, starting_columns):
        line = []
        if 0 <= col < columns:
            for current_col in range(col, col + 4):
                if 0 <= current_col < columns:
                    line.append(board[row][current_col])
            if line.count(line[0]) == 4:
                return True
    return False


def in_column(board, starting_row, starting_column):
    """
    Check the horizontal pipe if we have a winner.
    :param board: matrix
    :param starting_row: position of the player (row)
    :param starting_column: position of the player (col)
    :return: True or False, depends if we have a winner or not
    """
    rows = len(board)
    for row in range(starting_row - 3, starting_row + 1):
        line = []
        if 0 <= row < rows:
            for current_row in range(row, row + 4):
                if 0 <= current_row < rows:
                    line.append(board[current_row][starting_column - 1])
            if line.count(line[0]) == 4:
                return True
    return False


def validator(row, rows, col, columns):
    """
    This is a checker if row and col are valid
    :param row: row
    :param rows: total rows
    :param col: column
    :param columns: total columns
    :return: True or False
    """
    if 0 <= row < rows and 0 <= col < columns:
        return True
    return False


def in_diagonals(board, starting_row, starting_column, columns):
    """
    Check if we have a winner in the diagonals of the matrix (only the closest one which are in 4 steps of the player option)
    :param board: matrix
    :param starting_row: row of the player choice
    :param starting_column: col of the player choice
    :param columns: total columns
    :return: True or False
    """

    rows = len(board)
    line = []
    left_top_row_index = starting_row - 3
    left_top_col_index = starting_column - 3

    while left_top_row_index <= starting_row:
        if not validator(left_top_row_index, rows, left_top_col_index, columns):
            left_top_row_index += 1
            left_top_col_index += 1
            continue
        for i in range(4):
            row = left_top_row_index + i
            col = left_top_col_index + i
            if validator(row, rows, col, columns):
                line.append(board[row][col])
        if line.count(line[0]) == 4:
            return True
        left_top_row_index += 1
        left_top_col_index += 1
        line = []

    right_top_row_index = starting_row - 3
    right_top_col_index = starting_column + 3
    line = []

    while right_top_row_index <= starting_row:
        if not validator(right_top_row_index, rows, right_top_col_index, columns):
            right_top_row_index += 1
            right_top_col_index -= 1
            continue
        for i in range(4):
            row = right_top_row_index + i
            col = right_top_col_index - i
            if validator(row, rows, col, columns):
                line.append(board[row][col])
        if line.count(line[0]) == 4:
            return True
        right_top_row_index += 1
        right_top_col_index -= 1
        line = []

    return False


def is_winner(board, row, starting_column, columns):
    """
    When the player choice is acceptable, we check if he/she wins the game with this choice.
    :param board: matrix of the game
    :param row: current row
    :param starting_column: current col
    :param columns: total columns
    :return: if the player wins the game in one of the option, the game directly stop, if not - continue
    """
    if in_line(board, row, starting_column, columns):
        print(f"The winner is player {board[row][starting_column - 1]}")
        exit()
    if in_column(board, row, starting_column):
        print(f"The winner is player {board[row][starting_column - 1]}")
        exit()
    if in_diagonals(board, row, starting_column - 1, columns):
        print(f"The winner is player {board[row][starting_column - 1]}")
        exit()


def print_the_board(board):
    """
    After each step, we print the board for the next player. He can check it and decide where wants to put his option.
    :param board: matrix
    :return: None
    """
    for line in board:
        print(*line)


rows = 6
columns = 7
players = int(players_option())
board = [[0 for _ in range(columns)] for _ in range(rows)]

print_the_board(board)

while while_working(board):
    for current_player in range(1, players + 1):
        column_choice, row = choose_column(columns, current_player, board)
        board[row][column_choice - 1] = current_player
        is_winner(board, row, column_choice, columns)
        print_the_board(board)

print('There is no winner!')
