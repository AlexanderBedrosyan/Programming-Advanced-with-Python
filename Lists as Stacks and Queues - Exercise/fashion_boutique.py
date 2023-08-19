from collections import deque

clothes_current = [int(ch) for ch in input().split(" ")]
clothes = deque(clothes_current)
racks = int(input())

current_racks = racks
count = 1

while clothes:
    ch = clothes.pop()
    if current_racks == 0:
        count += 1
        current_racks = racks

    if ch <= current_racks:
        current_racks -= ch
    elif ch > current_racks:
        count += 1
        current_racks = racks
        current_racks -= ch

print(count)