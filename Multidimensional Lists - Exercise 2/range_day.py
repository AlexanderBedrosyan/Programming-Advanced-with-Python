matrix = []
directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
targets_hit = 0
targets_hit_positions = []
targets = 0


def move(direction, steps):
    r = my_position[0] + (directions[direction][0] * steps)
    c = my_position[1] + (directions[direction][1] * steps)

    if not (0 <= r < 5 and 0 <= c < 5):
        return my_position
    if matrix[r][c] == 'x':
        return my_position

    return [r, c]


def shoot(direction):
    r = my_position[0] + directions[direction][0]
    c = my_position[1] + directions[direction][1]

    while 0 <= r < 5 and 0 <= c < 5:
        if matrix[r][c] == 'x':
            matrix[r][c] = '.'
            return [r, c]

        r += directions[direction][0]
        c += directions[direction][1]


for i in range(5):
    line = input().split(" ")
    matrix.append([ch for ch in line])

    if 'A' in line:
        my_position = [i, line.index('A')]
        matrix[i][my_position[1]] = '.'

    targets += line.count('x')

num = int(input())


for _ in range(num):
    command_info = input().split()

    if command_info[0] == 'move':
        my_position = move(command_info[1], int(command_info[2]))
    elif command_info[0] == 'shoot':
        target_down_pos = shoot(command_info[1])

        if target_down_pos:
            targets_hit_positions.append(target_down_pos)
            targets_hit += 1

        if targets_hit == targets:
            print(f'Training completed! All {targets} targets hit.')
            break

if targets_hit < targets:
    print(f'Training not completed! {targets - targets_hit} targets left.')


[print(target_pos) for target_pos in targets_hit_positions]