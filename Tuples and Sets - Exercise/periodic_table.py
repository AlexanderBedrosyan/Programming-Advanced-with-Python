def final_result(num):
    unique_periodic_table = set()
    for _ in range(num):
        [unique_periodic_table.add(ch) for ch in input().split(" ")]

    print('\n'.join(unique_periodic_table))


num = int(input())
final_result(num)