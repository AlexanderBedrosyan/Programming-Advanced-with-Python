from collections import deque


def magic_needed(result):
    if 100 <= result <= 199:
        return 'Gemstone'
    elif 200 <= result <= 299:
        return 'Porcelain Sculpture'
    elif 300 <= result <= 399:
        return 'Gold'
    elif 400 <= result <= 499:
        return 'Diamond Jewellery'
    return False


def new_sum(last_mat, first_mag, sum_of_both):
    if sum_of_both < 100:
        if sum_of_both % 2 == 0:
            last_mat *= 2
            first_mag *= 3
            sum_of_both = last_mat + first_mag
        else:
            sum_of_both *= 2
    elif sum_of_both > 499:
        sum_of_both /= 2
    return sum_of_both


def is_succeeded(magics):
    if 'Gemstone' in magics and 'Porcelain Sculpture' in magics:
        return True
    if 'Gold' in magics and 'Diamond Jewellery' in magics:
        return True
    return False


materials = deque(int(ch) for ch in input().split(' '))
Genie_magic_level = deque(int(ch) for ch in input().split(' '))
created_magic = {}

while materials and Genie_magic_level:
    last_materials = materials.pop()
    first_magic_level = Genie_magic_level.popleft()
    sum_of_both = last_materials + first_magic_level
    magic_issued = magic_needed(sum_of_both)

    if not magic_issued:
        sum_of_both = new_sum(last_materials, first_magic_level, sum_of_both)
        magic_issued = magic_needed(sum_of_both)
        if not magic_issued:
            continue

    if magic_issued not in created_magic:
        created_magic[magic_issued] = 0
    created_magic[magic_issued] += 1

if is_succeeded(created_magic):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(ch) for ch in materials)}")
if Genie_magic_level:
    print(f"Magic left: {', '.join(str(ch) for ch in Genie_magic_level)}")

if created_magic:
    for present, amount in sorted(created_magic.items(), key=lambda x: x[0]):
        print(f"{present}: {amount}")