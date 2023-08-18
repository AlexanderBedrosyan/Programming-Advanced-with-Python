from collections import deque

quantity_food = int(input())
sequence_orders = [int(ch) for ch in input().split()]

orders_queue = deque(sequence_orders)

print(max(orders_queue))

while len(orders_queue) > 0:
    ch = orders_queue.popleft()

    if ch <= quantity_food:
        quantity_food -= ch
    else:
        orders_queue.appendleft(ch)
        break

if len(orders_queue) > 0:
    print("Orders left:", end=" ")
    for ch in orders_queue:
        print(f"{ch}", end=" ")
else:
    print("Orders complete")
