matrix = []
rows = int(input())
moves_dict = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
bunny_position = []
final_position = []
counter = 0
way = None

for row in range(rows):
    line = input().split()

    if 'B' in line:
        bunny_position = [row, line.index('B')]

    matrix.append(line)


for direction, positions in moves_dict.items():
    row, col = [
        bunny_position[0] + positions[0],
        bunny_position[1] + positions[1]
    ]

    path = []
    collected_eggs = 0

    while 0 <= row < rows and 0 <= col < rows:
        if matrix[row][col] == 'X':
            break

        collected_eggs += int(matrix[row][col])
        path.append([row, col])

        row += positions[0]
        col += positions[1]

    if collected_eggs >= counter:
        counter = collected_eggs
        way = direction
        final_position = path

print(way)
for i in range(0, len(final_position)):
    print(final_position[i])
print(counter)
