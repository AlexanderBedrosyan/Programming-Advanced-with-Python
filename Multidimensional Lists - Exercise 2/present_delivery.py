number_of_presents = int(input())
size = int(input())
directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
matrix = []
nice_kids = 0
santa_position = []
counter = 0


for i in range(size):
    line = input().split(" ")
    matrix.append([ch for ch in line])

    if 'S' in line:
        santa_position = [i, line.index('S')]
        matrix[i][santa_position[1]] = '-'

    nice_kids += line.count('V')

while True:
    command = input()

    if command == "Christmas morning":
        matrix[santa_position[0]][santa_position[1]] = "S"
        break

    current_row = santa_position[0] + directions[command][0]
    current_col = santa_position[1] + directions[command][1]

    if 0 <= current_row < size and 0 <= current_col < size:
        santa_position[0] = current_row
        santa_position[1] = current_col

    if matrix[current_row][current_col] == "X":
        matrix[current_row][current_col] = "-"
    elif matrix[current_row][current_col] == "V":
        matrix[current_row][current_col] = "-"
        number_of_presents -= 1
        counter += 1
        nice_kids -= 1
        if number_of_presents <= 0:
            print(f"Santa ran out of presents!")
            matrix[santa_position[0]][santa_position[1]] = "S"
            break
    elif matrix[current_row][current_col] == "C":
        for keys, values in directions.items():
            row = santa_position[0] + values[0]
            col = santa_position[1] + values[1]
            if 0 <= row < size and 0 <= col < size:
                if matrix[row][col] == "V":
                    number_of_presents -= 1
                    matrix[row][col] = "-"
                    nice_kids -= 1
                    counter += 1
                elif matrix[row][col] == "X":
                    number_of_presents -= 1
                    matrix[row][col] = "-"
            if number_of_presents <= 0:
                print(f"Santa ran out of presents!")
                matrix[santa_position[0]][santa_position[1]] = "S"
                break

    if number_of_presents <= 0:
        matrix[santa_position[0]][santa_position[1]] = "S"
        break

for ch in matrix:
    print(' '.join(chart for chart in ch))
if nice_kids == 0:
    print(f"Good job, Santa! {counter} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")