from collections import deque

working_bees = deque([int(ch) for ch in input().split(" ")])
nectar = [int(ch) for ch in input().split(" ")]
symbols = deque([ch for ch in input().split(" ")])
result = 0

while len(working_bees) > 0 and len(nectar) > 0:
    bee = working_bees.popleft()
    amount_nectar = nectar.pop()
    if bee > amount_nectar:
        working_bees.appendleft(bee)
        continue

    if amount_nectar == 0:
        continue
    elif amount_nectar > bee:
        need_symbol = symbols.popleft()
        current_result = 0
        if need_symbol == "+":
            current_result = abs(bee + amount_nectar)
        elif need_symbol == "-":
            current_result = abs(bee - amount_nectar)
        elif need_symbol == "*":
            current_result = abs(bee * amount_nectar)
        elif need_symbol == "/":
            current_result = abs(bee / amount_nectar)
        result += current_result

print(f"Total honey made: {result}")
if len(working_bees):
    print(f"Bees left: {', '.join(str(ch) for ch in working_bees)}")
if len(nectar):
    print(f"Nectar left: {', '.join(str(ch) for ch in nectar)}")