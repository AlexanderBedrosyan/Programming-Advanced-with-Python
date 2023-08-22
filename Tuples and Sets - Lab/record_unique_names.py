def final_result(num):
    tuple = set()
    for i in range(num):
        tuple.add(input())
    print('\n'.join(tuple))


num = int(input())
final_result(num)