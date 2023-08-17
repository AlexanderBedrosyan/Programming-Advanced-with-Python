from collections import deque

players = input().split(" ")
players_deque = deque(players)
game = int(input())
pass_ball = 1

while len(players_deque) > 1:
    person = players_deque.popleft()

    if pass_ball == game:
        print(f"Removed {person}")
        pass_ball = 1
        continue
    else:
        players_deque.append(person)
        pass_ball += 1

print(f"Last is {players_deque[0]}")
