from collections import deque


def best_list_pureness(*args):
    list_of_numbers = deque(args[0])
    k = args[1]
    rotation_best = 0
    total_score = sum([list_of_numbers[i] * i for i in range(len(list_of_numbers))])
    for index in range(k):
        last_element = list_of_numbers.pop()
        list_of_numbers.appendleft(last_element)
        current_score = sum([list_of_numbers[i] * i for i in range(len(list_of_numbers))])
        if current_score > total_score:
            total_score = current_score
            rotation_best = index + 1
    return f"Best pureness {total_score} after {rotation_best} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
