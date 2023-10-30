from collections import deque


def final(monsters, attackers, kills_counter):
    if not monsters:
        print('All monsters have been killed!')
    if not attackers:
        print("The soldier has been defeated.")
    print(f"Total monsters killed: {kills_counter}")


def attack_result(armor, damage):
    return damage - armor


armor_of_the_monsters = deque(int(ch) for ch in input().split(','))
soldier_striking_impact = deque(int(ch) for ch in input().split(','))
count_of_killed_monsters = 0

while armor_of_the_monsters and soldier_striking_impact:
    first_armor_value = armor_of_the_monsters.popleft()
    last_strike_strength_value = soldier_striking_impact.pop()
    result = attack_result(first_armor_value, last_strike_strength_value)

    if result >= 0:
        count_of_killed_monsters += 1
        if result == 0:
            continue
        try:
            current_last_strike = soldier_striking_impact.pop()
            new_attack = current_last_strike + result
            soldier_striking_impact.append(new_attack)
        except IndexError:
            soldier_striking_impact.append(result)
    elif result < 0:
        armor_of_the_monsters.append(abs(result))

final(armor_of_the_monsters, soldier_striking_impact, count_of_killed_monsters)