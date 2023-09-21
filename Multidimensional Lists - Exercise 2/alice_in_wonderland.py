rows = int(input())
matrix = []
moves_dict = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
needed_bags = 10
row_current = 0
col_current = 0
rabbit_or_out = False

for _ in range(rows):
    matrix.append([ch for ch in input().split(" ")])

for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == "A":
            row_current = row
            col_current = col
            matrix[row][col] = "*"


while True:
    command = input()
    row_current += moves_dict[command][0]
    col_current += moves_dict[command][1]

    if 0 <= row_current < rows and 0 <= col_current < rows:
        if matrix[row_current][col_current] != "R" and matrix[row_current][col_current] != "." \
                and matrix[row_current][col_current] != "*":
            needed_bags -= int(matrix[row_current][col_current])
            matrix[row_current][col_current] = "*"
            if needed_bags <= 0:
                print("She did it! She went to the party.")
                break
        elif matrix[row_current][col_current] != "R" and matrix[row_current][col_current] == ".":
            matrix[row_current][col_current] = "*"
        elif matrix[row_current][col_current] == "R":
            matrix[row_current][col_current] = "*"
            rabbit_or_out = True
    else:
        rabbit_or_out = True

    if rabbit_or_out:
        print("Alice didn't make it to the tea party.")
        break

for ch in matrix:
    print(' '.join(ch))