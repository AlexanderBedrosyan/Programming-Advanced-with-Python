rows = int(input())
battle_field = []
submarine_position = []
directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
hit_by_mine = 0
battle_cruisers = 3

for row in range(rows):
    line = [ch for ch in input()]
    if "S" in line:
        current_col = line.index("S")
        submarine_position.append([row, current_col])
    battle_field.append(line)

battle_field[submarine_position[0][0]][submarine_position[0][1]] = "-"

while battle_cruisers > 0 and hit_by_mine < 3:
    course = input()
    current_coordinates = submarine_position.pop(0)
    row = current_coordinates[0] + directions[course][0]
    col = current_coordinates[1] + directions[course][1]

    if battle_field[row][col] == "*":
        hit_by_mine += 1
        if hit_by_mine == 3:
            battle_field[row][col] = "S"
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!")
            for ch in battle_field:
                print(*ch, sep="")
            break
        else:
            battle_field[row][col] = "-"

    elif battle_field[row][col] == "C":
        battle_cruisers -= 1
        if battle_cruisers == 0:
            battle_field[row][col] = "S"
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            for ch in battle_field:
                print(*ch, sep="")
            break
        else:
            battle_field[row][col] = "-"

    submarine_position.append([row, col])
