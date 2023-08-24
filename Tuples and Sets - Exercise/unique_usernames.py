def final_result(num):
    unique_set = set()
    for i in range(num):
        unique_set.add(input())

    [print(ch) for ch in unique_set]


num = int(input())

final_result(num)