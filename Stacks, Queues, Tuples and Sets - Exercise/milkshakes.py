from collections import deque

chocolates = deque([int(ch) for ch in input().split(", ")])
cups_of_milk = deque([int(ch) for ch in input().split(", ")])

count = 0

while True:
    if count == 5:
        break
    elif len(chocolates) == 0 or len(cups_of_milk) == 0:
        break

    chocolates_ch = chocolates.pop()
    cups_ch = cups_of_milk.popleft()

    if chocolates_ch <= 0 and cups_ch <= 0:
        continue
    if cups_ch <= 0:
        chocolates.append(chocolates_ch)
        continue
    if chocolates_ch <= 0:
        cups_of_milk.appendleft(cups_ch)
        continue

    if chocolates_ch == cups_ch:
        count += 1
        continue
    else:
        cups_of_milk.append(cups_ch)
        chocolates_ch -= 5
        if chocolates_ch <= 0:
            continue
        chocolates.append(chocolates_ch)

if count == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if len(chocolates) > 0:
    print(f"Chocolate: {', '.join([str(num) for num in chocolates])}")
else:
    print("Chocolate: empty")

if len(cups_of_milk) > 0:
    print(f"Milk: {', '.join([str(num) for num in cups_of_milk])}")
else:
    print("Milk: empty")
