from collections import deque

robots = input().split(";")
clock = [int(ch) for ch in input().split(":")]
free_robots = {}
working_robots = {}

elements_for_work = deque()

for ch in robots:
    new_ch = ch.split("-")
    robots = new_ch[0]
    seconds = int(new_ch[1])
    free_robots[robots] = seconds

while True:
    elements = input()

    if elements == "End":
        break

    elements_for_work.append(elements)

while elements_for_work:
    current_element = elements_for_work.popleft()
    clock[2] += 1

    if clock[2] == 60:
        clock[1] += 1
        clock[2] = 0
        if clock[1] == 60:
            clock[1] = 0
            clock[0] += 1
            if clock[0] == 24:
                clock[0] = 0

    for i in working_robots:
        working_robots[i] += 1

    for key in free_robots:
        if key in working_robots:
            if working_robots[key] == free_robots[key]:
                del working_robots[key]

    if len(free_robots) != len(working_robots):
        for chart in free_robots:
            if chart not in working_robots:
                print(f"{chart} - {current_element} [{clock[0]:02d}:{clock[1]:02d}:{clock[2]:02d}]")
                working_robots[chart] = 0
                break
    else:
        elements_for_work.append(current_element)
