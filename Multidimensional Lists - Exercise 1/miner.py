rows = int(input())
commands = [ch for ch in input().split(" ")]
matrix = []
commands_dict = {"up": [-1, 0], "down": [1, 0], "right": [0, 1], "left": [0, -1]}
position = []
coals = 0

for _ in range(rows):
    matrix.append([ch for ch in input().split(" ")])

for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == "s":
            position.append(row)
            position.append(col)
        elif matrix[row][col] == "c":
            coals += 1

for i in range(len(commands)):
    current_row = 0
    current_col = 0
    if commands[i] in commands_dict:
        current_row, current_col = commands_dict[commands[i]][0], commands_dict[commands[i]][1]

    if 0 <= position[0] + current_row < rows and 0 <= position[1] + current_col < rows:
        position[0] += current_row
        position[1] += current_col
        if matrix[position[0]][position[1]] == "c":
            coals -= 1
            matrix[position[0]][position[1]] = "*"
            if coals == 0:
                print(f"You collected all coal! ({position[0]}, {position[1]})")
                exit()
        elif matrix[position[0]][position[1]] == "e":
            print(f"Game over! ({position[0]}, {position[1]})")
            exit()

print(f"{coals} pieces of coal left. ({position[0]}, {position[1]})")
