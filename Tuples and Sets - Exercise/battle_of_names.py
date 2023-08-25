def odd_or_even(num):
    odd = set()
    even = set()
    count = 0

    for _ in range(num):
        count += 1
        name = input()
        total_amount = 0
        for ch in name:
            total_amount += ord(ch)

        total_amount = total_amount // count

        if total_amount % 2 == 0:
            even.add(total_amount)
        else:
            odd.add(total_amount)

    return odd, even


def final_result(odd, even):
    if sum(odd) == sum(even):
        union_combination = odd.union(even)
        print(*union_combination, sep=", ")

    elif sum(odd) > sum(even):
        difference_combination = odd.difference(even)
        print(*difference_combination, sep=", ")

    else:
        symmetric = odd.symmetric_difference(even)
        print(*symmetric, sep=", ")


num = int(input())
odd_set = set()
even_set = set()

odd_set, even_set = odd_or_even(num)

final_result(odd_set, even_set)
