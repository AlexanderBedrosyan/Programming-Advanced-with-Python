from collections import deque


def fill_the_box(*args):
    current_list = deque(args)
    cube_result = current_list.popleft() * current_list.popleft() * current_list.popleft()
    for ch in current_list:
        if ch == "Finish":
            break
        else:
            cube_result -= ch

    if cube_result > 0:
        return f"There is free space in the box. You could put {cube_result} more cubes."
    else:
        return f"No more free space! You have {abs(cube_result)} more cubes."


print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))

