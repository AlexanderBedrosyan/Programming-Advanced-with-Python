from collections import deque


def check_if_perfect_firework_show(fireworks_dict):
    for values in fireworks_dict.values():
        if values < 3:
            return False
    return True


def try_to_create_firework(firework_eff, explosive_pow):
    sum_of_values = firework_eff + explosive_pow
    if sum_of_values % 3 == 0 and sum_of_values % 5 == 0:
        return f"Crossette Fireworks"
    elif sum_of_values % 3 != 0 and sum_of_values % 5 == 0:
        return f"Willow Fireworks"
    elif sum_of_values % 3 == 0 and sum_of_values % 5 != 0:
        return f"Palm Fireworks"
    return None


firework_effects = deque(int(ch) for ch in input().split(', '))
explosive_power = deque(int(ch) for ch in input().split(', '))

fireworks = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0,
}
perfect_show = False

while firework_effects and explosive_power:
    first_firework_effect = firework_effects.popleft()
    if first_firework_effect <= 0:
        continue
    last_explosive_power = explosive_power.pop()
    if last_explosive_power <= 0:
        firework_effects.appendleft(first_firework_effect)
        continue

    firework_type = try_to_create_firework(first_firework_effect, last_explosive_power)

    if firework_type is not None:
        fireworks[firework_type] += 1
        if check_if_perfect_firework_show(fireworks):
            perfect_show = True
            break
        continue

    first_firework_effect -= 1
    firework_effects.append(first_firework_effect)
    explosive_power.append(last_explosive_power)

if perfect_show:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(str(element) for element in firework_effects)}")

if explosive_power:
    print(f"Explosive Power left: {', '.join(str(element) for element in explosive_power)}")

for firework_type, counter in fireworks.items():
    print(f"{firework_type}: {counter}")
