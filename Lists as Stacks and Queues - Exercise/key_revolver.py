from collections import deque

price_per_bullet = int(input())
gun_barrel_size = int(input())
list_bullets = [int(ch) for ch in input().split(" ")]
bullets = deque(list_bullets)
list_locks = [int(ch) for ch in input().split(" ")]
locks = deque(list_locks)
total_price = int(input())
count = 0

while len(bullets) > 0 and len(locks) > 0:
    current_bullets = bullets.pop()
    current_locks = locks.popleft()

    if current_bullets <= current_locks:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(current_locks)

    count += 1
    total_price -= price_per_bullet
    if gun_barrel_size == count and len(bullets) > 0:
        print("Reloading!")
        count = 0

if len(locks) == 0:
    print(f"{len(bullets)} bullets left. Earned ${total_price}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
