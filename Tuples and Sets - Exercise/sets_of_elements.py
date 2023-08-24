def n_set(n):
    first_set = set()
    for _ in range(n):
        first_set.add(input())
    return first_set


def m_set(m):
    second_set = set()
    for _ in range(m):
        second_set.add(input())
    return second_set


def final_result(set1, set2):
    intersection = set1.intersection(set2)
    [print(ch) for ch in intersection]


n, m = [int(ch) for ch in input().split(" ")]

first_set = n_set(n)
second_set = m_set(m)

final_result(first_set, second_set)