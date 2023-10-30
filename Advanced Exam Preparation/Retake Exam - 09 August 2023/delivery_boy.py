def valid(rows, columns, row, col):
    if 0 <= row < rows and 0 <= col < columns:
        return True
    return False


def final(matrix):
    for line in matrix:
        print(''.join(line))


rows, columns = [int(ch) for ch in input().split(' ')]
neighborhood = [[ch for ch in input()] for _ in range(rows)]

delivery_boy_position = [[row, col] for col in range(columns) for row in range(rows) if neighborhood[row][col] == 'B'][0]
starting_position = [int(ch) for ch in delivery_boy_position]
directions = {
    "left": [0, -1],
    "right": [0, 1],
    "down": [1, 0],
    "up": [-1, 0]
}
collected_pizza = False

while True:
    command = input()
    row = directions[command][0] + delivery_boy_position[0]
    col = directions[command][1] + delivery_boy_position[1]

    if not valid(rows, columns, row, col):
        print("The delivery is late. Order is canceled.")
        neighborhood[starting_position[0]][starting_position[1]] = ' '
        break

    if neighborhood[row][col] == 'P':
        print("Pizza is collected. 10 minutes for delivery.")
        collected_pizza = True
        neighborhood[row][col] = 'R'
    elif neighborhood[row][col] == '*':
        continue
    elif neighborhood[row][col] == 'A' and collected_pizza:
        neighborhood[row][col] = 'P'
        print('Pizza is delivered on time! Next order...')
        neighborhood[starting_position[0]][starting_position[1]] = 'B'
        break
    elif neighborhood[row][col] == '-':
        neighborhood[row][col] = '.'
    delivery_boy_position = [row, col]

final(neighborhood)