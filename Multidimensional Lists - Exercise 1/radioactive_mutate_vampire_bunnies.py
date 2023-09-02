rows, columns = (int(ch) for ch in input().split(" "))
matrix = []
commands_dict = {"U": [-1, 0], "D": [1, 0], "R": [0, 1], "L": [0, -1]}
bunny_position = []
player_position = []
alive_player = False
won = False

for _ in range(rows):
    matrix.append([ch for ch in input() if ch in ['.', 'B', 'P']])

commands = [ch for ch in input()]

for row in range(rows):
    for col in range(columns):
        if matrix[row][col] == "P":
            player_position.append(row)
            player_position.append(col)

for i in range(len(commands)):
    if commands[i] in commands_dict:
        row = player_position[0] + commands_dict[commands[i]][0]
        col = player_position[1] + commands_dict[commands[i]][1]
        if 0 <= row < rows and 0 <= col < columns:
            matrix[player_position[0]][player_position[1]] = "."
            player_position[0] = row
            player_position[1] = col
            if matrix[row][col] != "B":
                matrix[row][col] = "P"
        else:
            won = True
            matrix[player_position[0]][player_position[1]] = "."

    for row in range(rows):
        for col in range(columns):
            if matrix[row][col] == "B":
                bunny_position.append([row, col])

    for j in range(len(bunny_position)):
        for ch in commands_dict:
            row_b = bunny_position[j][0] + commands_dict[ch][0]
            col_b = bunny_position[j][1] + commands_dict[ch][1]
            if 0 <= row_b < rows and 0 <= col_b < columns:
                matrix[row_b][col_b] = "B"

    count_if_alive = 0

    for k in range(len(matrix)):
        if "P" in matrix[k]:
            count_if_alive += 1

    if count_if_alive == 0:
        alive_player = False
    else:
        alive_player = True

    if not alive_player and not won:
        for l in range(len(matrix)):
            print(''.join(matrix[l]))
        print(f"dead: {player_position[0]} {player_position[1]}")
        break

    if won:
        for n in range(len(matrix)):
            print(''.join(matrix[n]))
        print(f"won: {player_position[0]} {player_position[1]}")
        break
