from collections import deque

materials_for_crafting_toys = deque([int(ch) for ch in input().split(" ")])
magic_level = deque([int(ch) for ch in input().split(" ")])

dictionary_magic = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}
craft_dict = {}

while len(materials_for_crafting_toys) > 0 and len(magic_level) > 0 and len(dictionary_magic) > 0:
    material = materials_for_crafting_toys.pop()
    magic = magic_level.popleft()

    current_sum = material * magic

    if current_sum < 0:
        current_sum = material + magic
        materials_for_crafting_toys.append(current_sum)
        continue

    if current_sum == 0:
        if material == 0 and magic == 0:
            continue
        elif material == 0 and magic != 0:
            magic_level.appendleft(magic)
            continue
        elif material != 0 and magic == 0:
            materials_for_crafting_toys.append(material)
            continue

    if current_sum not in dictionary_magic and current_sum > 0:
        material += 15
        materials_for_crafting_toys.append(material)
        continue
    elif current_sum in dictionary_magic and current_sum > 0:
        if dictionary_magic[current_sum] not in craft_dict:
            craft_dict[dictionary_magic[current_sum]] = 0
        craft_dict[dictionary_magic[current_sum]] += 1
        continue

if ("Doll" in craft_dict and "Wood train" in craft_dict) or ("Teddy bear" in craft_dict and "Bicycle" in craft_dict):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if len(materials_for_crafting_toys) > 0:
    print(f"Materials left: {', '.join(str(ch) for ch in reversed(materials_for_crafting_toys))}")

if len(magic_level) > 0:
    print(f"Magic left: {', '.join(str(ch) for ch in magic_level)}")

for ch in sorted(craft_dict):
    print(f"{ch}: {craft_dict[ch]}")
