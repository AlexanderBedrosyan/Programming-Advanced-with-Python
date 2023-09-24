rows = int(input())
matrix = []
knight_move = {"move1": [-2, -1], "move2": [-1, -2], "move3": [-2, 1], "move4": [-1, 2],
               "move5": [1, -2], "move6": [2, -1], "move7": [2, 1], "move8": [1, 2]}

for _ in range(rows):
    matrix.append([ch for ch in input()])

column = len(matrix[0])
horses_dict = {}
counter = 0

while True:
    for row in range(rows):
        for col in range(column):
            if matrix[row][col] == "K":
                current_hits = 0
                for ch in knight_move:
                    current_row = row + knight_move[ch][0]
                    current_col = col + knight_move[ch][1]
                    if 0 <= current_row < rows and 0 <= current_col < column:
                        if matrix[current_row][current_col] == "K":
                            current_hits += 1
                if current_hits > 0:
                    if len(horses_dict) == 0:
                        horses_dict[current_hits] = [row, col]
                    elif current_hits in horses_dict:
                        continue
                    else:
                        for key in horses_dict:
                            if key < current_hits:
                                horses_dict = {}
                                horses_dict[current_hits] = [row, col]

    if len(horses_dict) == 0:
        break
    else:
        for ch in horses_dict:
            matrix[horses_dict[ch][0]][horses_dict[ch][1]] = 0
            counter += 1

    horses_dict = {}

print(counter)
