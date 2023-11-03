def creating_the_board_and_find_the_position_of_squirrel(size):
    current_board = []
    squirrel_position = []

    for row in range(size):
        line = [ch for ch in input()]
        if "s" in line:
            ind = line.index("s")
            squirrel_position.append([row, ind])
            line[ind] = "*"
        current_board.append(line)
    return current_board, squirrel_position


def print_the_final_result(text, counter):
    print(text)
    print(f"Hazelnuts collected: {counter}")


def steps_into_the_game(row_col, steps_direction, dict_directions, field, the_squirrel_position):
    counter_hazelnut = 0
    result = False
    while True:
        for ch in steps_direction:
            row = the_squirrel_position[0][0] + dict_directions[ch][0]
            col = the_squirrel_position[0][1] + dict_directions[ch][1]
            if 0 <= row < row_col and 0 <= col < row_col:
                if field[row][col] == "h":
                    counter_hazelnut += 1
                    field[row][col] = "*"
                    if counter_hazelnut == 3:
                        result = True
                        print_the_final_result("Good job! You have collected all hazelnuts!", counter_hazelnut)
                        break
                elif field[row][col] == "t":
                    result = True
                    print_the_final_result("Unfortunately, the squirrel stepped on a trap...", counter_hazelnut)
                    break
                the_squirrel_position = []
                the_squirrel_position.append([row, col])
            else:
                result = True
                print_the_final_result("The squirrel is out of the field.", counter_hazelnut)
                break
        break
    if not result:
        print_the_final_result("There are more hazelnuts to collect.", counter_hazelnut)


size = int(input())
commands = [ch for ch in input().split(", ")]
directions = {"left": [0, -1], "right": [0, 1], "down": [1, 0], "up": [-1, 0]}
board = []
squirrel_position = []

board, squirrel_position = creating_the_board_and_find_the_position_of_squirrel(size)
steps_into_the_game(size, commands, directions, board, squirrel_position)
