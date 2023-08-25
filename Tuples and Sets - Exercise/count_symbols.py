from collections import deque


def final_result(list):
    letters_dict = {}
    for ch in sorted(list):
        if ch not in letters_dict:
            letters_dict[ch] = 0
        letters_dict[ch] += 1
    for key, values in letters_dict.items():
        print(f"{key}: {values} time/s")


letters = deque([ch for ch in input()])

final_result(letters)