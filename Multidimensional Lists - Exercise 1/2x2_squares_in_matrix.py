rows, cols = (int(ch) for ch in input().split(" "))
matrix = []
counter = 0

for _ in range(rows):
    matrix.append([ch for ch in input().split(" ")])

for row in range(rows - 1):
    current_square = []
    current_counter = True
    for col in range(cols - 1):
        current_square.append([matrix[row][col], matrix[row][col + 1],
                               matrix[row + 1][col], matrix[row + 1][col + 1]])

        needed_chart = current_square[0][0]

        for ch in current_square[0]:
            if ch == needed_chart:
                continue
            else:
                current_counter = False
                break

        if current_counter:
            counter += 1

        current_square = []
        current_counter = True

print(counter)
