rows, columns = [int(ch) for ch in input().split(" ")]
board = []
B_position = []
P_position = []
directions = {"up": [-1, 0], "down": [1, 0],"right": [0, 1], "left": [0, -1]}
moves_made = 0
touched_opponents = 0

for row in range(rows):
    line = input().split(" ")
    if "B" in line:
        ind = line.index("B")
        B_position.append([row, ind])
        line[ind] = "-"
    if "P" in line:
        p_ind = line.index("P")
        P_position.append([row, p_ind])
    board.append(line)

while True:
    command = input()

    if command == "Finish":
        break

    current_row = B_position[0][0] + directions[command][0]
    current_col = B_position[0][1] + directions[command][1]

    if 0 <= current_row < rows and 0 <= current_col < columns:
        if board[current_row][current_col] == "O":
            continue
        elif board[current_row][current_col] == "-":
            moves_made += 1
            B_position = []
            B_position.append([current_row, current_col])
        elif board[current_row][current_col] == "P":
            board[current_row][current_col] = "-"
            moves_made += 1
            touched_opponents += 1
            B_position = []
            B_position.append([current_row, current_col])
            if touched_opponents == 3:
                break
    else:
        continue

print(f"Game over!\nTouched opponents: {touched_opponents} Moves made: {moves_made}")
