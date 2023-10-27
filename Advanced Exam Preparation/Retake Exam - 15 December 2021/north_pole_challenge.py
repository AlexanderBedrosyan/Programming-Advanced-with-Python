def correct_position(row, rows, col, columns):
    if row < 0:
        row = rows - 1
    if row == rows:
        row = 0
    if col < 0:
        col = columns - 1
    if col == columns:
        col = 0
    return row, col


def from_letter_to_word(letter):
    dict_of_words = {
        'D': 'Christmas decorations',
        'G': 'Gifts',
        'C': 'Cookies'
    }
    return dict_of_words[letter]

directions = {"left": [0, -1], "right": [0, 1], "up": [-1, 0], "down": [1, 0]}


rows, columns = [int(ch) for ch in input().split(', ')]
north_pole = [[ch for ch in input().split(' ')] for _ in range(rows)]
player_position = [[row, col] for col in range(columns) for row in range(rows) if north_pole[row][col] == 'Y'][0]
all_items = sum([1 for col in range(columns) for row in range(rows) if north_pole[row][col] in 'DGC'])
north_pole[player_position[0]][player_position[1]] = 'x'
collected_items = {
    'Christmas decorations': 0,
    'Gifts': 0,
    'Cookies': 0
}

command = input()

while command != 'End':
    command = command.split('-')
    direct, steps = command[0], int(command[1])
    all_items_collected = False

    for step in range(steps):
        current_direction = directions[direct]
        row = player_position[0] + current_direction[0]
        col = player_position[1] + current_direction[1]
        row, col = correct_position(row, rows, col, columns)
        if north_pole[row][col] in 'DGC':
            word = from_letter_to_word(north_pole[row][col])
            all_items -= 1
            collected_items[word] += 1
        north_pole[row][col] = 'x'
        player_position = [row, col]

        if all_items == 0:
            all_items_collected = True
            break

    if all_items_collected:
        break

    command = input()

if all_items == 0:
    print('Merry Christmas!')
print("You've collected:")
for key, value in collected_items.items():
    print(f'- {value} {key}')

north_pole[player_position[0]][player_position[1]] = 'Y'
for line in north_pole:
    print(' '.join(line))