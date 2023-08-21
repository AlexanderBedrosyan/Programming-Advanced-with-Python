from collections import deque

cups = deque([int(ch) for ch in input().split(" ")])
bottles = deque([int(ch) for ch in input().split(" ")])
wasted_water = 0

while len(cups) > 0 and len(bottles) > 0:
    first_cup = cups.popleft()
    first_bottle = bottles.pop()
    result = first_cup - first_bottle

    if result <= 0:
        wasted_water -= result
    else:
        cups.appendleft(result)

if len(cups) == 0:
    new_bottles = []
    for ch in bottles:
        new_bottles.append(str(ch))
    print(f"Bottles: {' '.join(new_bottles[::-1])}")
    print(f"Wasted litters of water: {wasted_water}")
else:
    new_cups = []
    for ch in cups:
        new_cups.append(str(ch))
    print(f"Cups: {' '.join(new_cups)}")
    print(f"Wasted litters of water: {wasted_water}")
