from collections import deque


def is_enough(energy, needed_energy):
    return energy >= needed_energy


elf_energy = deque(int(ch) for ch in input().split(' '))
materials_in_a_box = deque(int(ch) for ch in input().split(' '))

total_elfs_energy_used = 0
successfully_made_toys = 0
counter = 0

while elf_energy and materials_in_a_box:
    first_elf_energy = elf_energy.popleft()
    if first_elf_energy < 5:
        continue
    last_box_material = materials_in_a_box.pop()
    counter += 1

    if is_enough(first_elf_energy, last_box_material) and not (counter % 3 == 0 or counter % 5 == 0):
        first_elf_energy -= last_box_material
        elf_energy.append(first_elf_energy + 1)
        successfully_made_toys += 1
        total_elfs_energy_used += last_box_material
        continue

    if counter % 3 == 0 and is_enough(first_elf_energy, last_box_material * 2):
        if counter % 5 != 0:
            successfully_made_toys += 2
            first_elf_energy -= (2 * last_box_material)
            elf_energy.append(first_elf_energy + 1)
        else:
            first_elf_energy -= 2 * last_box_material
            elf_energy.append(first_elf_energy)
        total_elfs_energy_used += 2 * last_box_material
        continue

    if counter % 5 == 0 and is_enough(first_elf_energy, last_box_material) and counter % 3 != 0:
        first_elf_energy -= last_box_material
        elf_energy.append(first_elf_energy)
        total_elfs_energy_used += last_box_material
        continue

    first_elf_energy *= 2
    elf_energy.append(first_elf_energy)
    materials_in_a_box.append(last_box_material)

print(f"Toys: {successfully_made_toys}")
print(f"Energy: {total_elfs_energy_used}")
if elf_energy:
    print(f"Elves left: {', '.join(str(ch) for ch in elf_energy)}")
if materials_in_a_box:
    print(f"Boxes left: {', '.join(str(ch) for ch in materials_in_a_box)}")
