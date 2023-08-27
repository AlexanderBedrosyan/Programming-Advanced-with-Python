from collections import deque

dict_secondary = {"orange": ["red", "yellow"], "purple": ["red", "blue"], "green": ["yellow", "blue"]}
main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]

matched_main = []

string_list = deque([ch for ch in input().split(" ")])

while len(string_list) > 0:
    current_string = ''
    reversed_current_string = ''
    if len(string_list) > 1:
        part_one = string_list.popleft()
        part_two = string_list.pop()
        current_string = part_one + part_two
        reversed_current_string = part_two + part_one
        if current_string in main_colors:
            matched_main.append(current_string)
            continue
        elif current_string in secondary_colors:
            matched_main.append(current_string)
            continue
        elif reversed_current_string in main_colors:
            matched_main.append(reversed_current_string)
        elif reversed_current_string in secondary_colors:
            matched_main.append(reversed_current_string)
        else:
            current_one = part_one[:-1]
            current_two = part_two[:-1]
            if len(string_list) > 1:
                index = len(string_list) // 2
                if current_two != "":
                    string_list.insert(index, current_two)
                if current_one != "":
                    string_list.insert(index, current_one)
            elif len(string_list) <= 1:
                if current_two != "":
                    string_list.appendleft(current_two)
                if current_one != "":
                    string_list.appendleft(current_one)
    else:
        part_one = string_list.popleft()
        current_string = part_one
        if current_string in main_colors:
            matched_main.append(current_string)
            continue
        elif current_string in secondary_colors:
            matched_main.append(current_string)
            continue
        else:
            current_one = part_one[:-1]
            if current_one != "":
                string_list.append(current_one)

final_list = []

for ch in matched_main:
    count = 0
    if ch in secondary_colors:
        for key in dict_secondary[ch]:
            if key in matched_main:
                count += 1
    else:
        final_list.append(ch)

    if count == 2:
        final_list.append(ch)

print(final_list)
