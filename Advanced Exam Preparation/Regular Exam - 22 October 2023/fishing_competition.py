def correct_position(row, col, size):
    if row < 0:
        row = size - 1
    if row == size:
        row = 0
    if col < 0:
        col = size - 1
    if col == size:
        col = 0
    return row, col


directions = {"up": [-1, 0], "down": [1, 0], "right": [0, 1], "left": [0, -1]}
size = int(input())
fishing_area = [[ch for ch in input()] for _ in range(size)]
my_position = [[row, col] for col in range(size) for row in range(size) if fishing_area[row][col] == "S"][0]
fishing_area[my_position[0]][my_position[1]] = "-"
collected_fishes = 0

command = input()

while command != "collect the nets":
    row = directions[command][0] + my_position[0]
    col = directions[command][1] + my_position[1]
    row, col = correct_position(row, col, size)
    my_position = [row, col]

    if fishing_area[row][col].isdigit():
        collected_fishes += int(fishing_area[row][col])
        fishing_area[row][col] = "-"
    elif fishing_area[row][col] == "W":
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
              f"Last coordinates of the ship: [{my_position[0]},{my_position[1]}]")
        exit()

    command = input()

fishing_area[my_position[0]][my_position[1]] = "S"
if collected_fishes >= 20:
    print("Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - collected_fishes} tons of fish more.")

if collected_fishes > 0:
    print(f"Amount of fish caught: {collected_fishes} tons.")

for line in fishing_area:
    print(''.join(line))
