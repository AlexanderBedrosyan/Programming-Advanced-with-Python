from collections import deque


def valid(current_female, current_male):
    """
    :param current_female: first female
    :param current_male: last male
    :return: if current_female and current_male are equal.
    """
    return current_male == current_female


males = deque(int(ch) for ch in input().split(' '))
females = deque(int(ch) for ch in input().split(' '))
matches = 0

while males and females:
    first_female = females.popleft()
    last_male = males.pop()
    if first_female <= 0:
        males.append(last_male)
        continue
    if last_male <= 0:
        females.appendleft(first_female)
        continue
    if first_female % 25 == 0:
        try:
            females.popleft()
            males.append(last_male)
            continue
        except IndexError:
            break
    if last_male % 25 == 0:
        try:
            males.pop()
            females.appendleft(first_female)
            continue
        except IndexError:
            break

    if valid(first_female, last_male):
        matches += 1
        continue

    last_male -= 2
    males.append(last_male)

print(f"Matches: {matches}")
if not males:
    print("Males left: none")
else:
    print(f"Males left: {', '.join(str(males[i]) for i in range(len(males) - 1, - 1, - 1))}")

if not females:
    print("Females left: none")
else:
    print(f"Females left: {', '.join(str(element) for element in females)}")
