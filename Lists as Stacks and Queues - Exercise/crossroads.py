from collections import deque

green_light = int(input())
free_window = int(input())
traffic_queue = deque()
count = 0
car_in_cross = ""
hit_place = ""

while True:
    command = input()
    current_green = green_light
    current_free = free_window

    if command == "END":
        break

    elif command == "green":
        while len(traffic_queue) > 0 and current_green > 0:
            ch = traffic_queue.popleft()
            if current_green > 0:
                count += 1
                current_green -= len(ch)
            if current_green < 0:
                current_free += current_green
                if current_free < 0:
                    idx = (-current_free)
                    car_in_cross = ch
                    hit_place = car_in_cross[-idx]
                    print(f"A crash happened!\n{car_in_cross} was hit at {hit_place}.")
                    exit()

    else:
        traffic_queue.append(command)

if len(car_in_cross) == 0:
    print(f"Everyone is safe.\n{count} total cars passed the crossroads.")