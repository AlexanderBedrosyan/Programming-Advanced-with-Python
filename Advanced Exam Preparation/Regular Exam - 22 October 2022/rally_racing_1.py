size = int(input())
racing_number = input()
race_route = []
car_coordinates = [[0, 0]]
tunnels_coordinates = []
kilometeres_passed = 0
directions = {"left": [0, -1], "right": [0, 1], "up": [-1, 0], "down": [1, 0]}
winner = False

for row in range(size):
    line = [ch for ch in input().split(" ")]
    for i in range(len(line)):
        if line[i] == "T":
            tunnels_coordinates.append([row, i])
    race_route.append(line)

while True:
    course = input()

    if course == "End":
        current_position = car_coordinates.pop(0)
        race_route[current_position[0]][current_position[1]] = "C"
        print(f"Racing car {racing_number} DNF.")
        break

    current_position = car_coordinates.pop(0)
    row = current_position[0] + directions[course][0]
    col = current_position[1] + directions[course][1]

    if race_route[row][col] == "F":
        race_route[row][col] = "C"
        kilometeres_passed += 10
        winner = True
        break
    elif race_route[row][col] == "T":
        current_coordinates = [row, col]
        new_coordinates = []
        for ch in tunnels_coordinates:
            if ch != current_coordinates:
                new_coordinates = ch
        car_coordinates.append(new_coordinates)
        kilometeres_passed += 30
        race_route[row][col] = "."
        race_route[new_coordinates[0]][new_coordinates[1]] = "."
        continue

    car_coordinates.append([row, col])
    kilometeres_passed += 10

if winner:
    print(f"Racing car {racing_number} finished the stage!")
print(f"Distance covered {kilometeres_passed} km.")
for ch in race_route:
    print(''.join(ch))
