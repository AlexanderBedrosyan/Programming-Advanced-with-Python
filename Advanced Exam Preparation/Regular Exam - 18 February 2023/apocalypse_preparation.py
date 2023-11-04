from collections import deque

textiles = deque([int(ch) for ch in input().split(" ")])
medicaments = deque([int(ch) for ch in input().split(" ")])

healing_dict = {"Patch": 30, "Bandage": 40, "MedKit": 100}
MEDKIT = 100
final_dict = {}

while len(textiles) > 0 and len(medicaments) > 0:
    first_textiles = textiles.popleft()
    last_medicaments = medicaments.pop()
    combine_elements = first_textiles + last_medicaments

    if combine_elements > MEDKIT:
        current_last_medicaments = medicaments.pop()
        current_last_medicaments += (combine_elements - MEDKIT)
        medicaments.append(current_last_medicaments)
        if "MedKit" not in final_dict:
            final_dict["MedKit"] = 0
        final_dict["MedKit"] += 1
        continue

    flag = False

    for item, resources in healing_dict.items():
        if resources == combine_elements:
            if item not in final_dict:
                final_dict[item] = 0
            final_dict[item] += 1
            flag = True

    if not flag:
        last_medicaments += 10
        medicaments.append(last_medicaments)


if len(textiles) == 0 and len(medicaments) == 0:
    print("Textiles and medicaments are both empty.")
elif len(textiles) == 0:
    print("Textiles are empty.")
elif len(medicaments) == 0:
    print("Medicaments are empty.")
if len(final_dict) > 0:
    for healing_items, amount in sorted(final_dict.items(), key=lambda x: (-x[1], x[0])):
        print(f"{healing_items} - {amount}")
if len(medicaments) > 0:
    current_list = []
    for ch in medicaments:
        current_list.append(ch)
    print(f"Medicaments left: {', '.join(str(ch) for ch in current_list[::-1])}")
if len(textiles) > 0:
    print(f"Textiles left: {', '.join(str(ch) for ch in textiles)}")
