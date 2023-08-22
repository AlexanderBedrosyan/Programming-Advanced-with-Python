def result(list):
    new_tuple = (list)
    current_tuple = []
    for chart in list:
        if chart not in current_tuple:
            current_tuple.append(chart)

    for ch in current_tuple:
        print(f"{ch} - {new_tuple.count(ch)} times")


numbers_list = [float(ch) for ch in input().split(" ")]

result(numbers_list)
