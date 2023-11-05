from collections import deque

bomb_effects = deque([int(ch) for ch in input().split(", ")])
bomb_casing = [int(ch) for ch in input().split(", ")]
dict_bombs = {"Datura Bombs": 40, "Cherry Bombs": 60, "Smoke Decoy Bombs": 120}
add_dict = {"Cherry Bombs": 0, "Datura Bombs": 0, "Smoke Decoy Bombs": 0}
condition = False

while len(bomb_casing) > 0 and len(bomb_effects) > 0:
    first_effects = bomb_effects.popleft()
    last_casting = bomb_casing.pop()
    current_result = first_effects + last_casting
    flag = False

    for ch in dict_bombs:
        if dict_bombs[ch] == current_result:
            flag = True
            add_dict[ch] += 1
            break

    if (add_dict["Cherry Bombs"] >= 3) and (add_dict["Datura Bombs"] >= 3) and (add_dict["Smoke Decoy Bombs"] >= 3):
        condition = True
        break

    if not flag:
        last_casting -= 5
        bomb_effects.appendleft(first_effects)
        bomb_casing.append(last_casting)


if not condition:
    print("You don't have enough materials to fill the bomb pouch.")
else:
    print("Bene! You have successfully filled the bomb pouch!")

if len(bomb_effects) == 0:
    print(f"Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join(str(ch) for ch in bomb_effects)}")

if len(bomb_casing) == 0:
    print(f"Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join(str(ch) for ch in bomb_casing)}")

for keys, values in add_dict.items():
    print(f"{keys}: {values}")