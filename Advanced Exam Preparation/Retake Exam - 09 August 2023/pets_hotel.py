def accommodate_new_pets(*args, **kwargs):
    result = []
    information_gather = {}
    available_capacity = int(args[0])
    maximum_weight_limit = float(args[1])
    pet_information = args[2:]
    pets_counter = 0
    for information in pet_information:
        type_of_pet = information[0]
        weight = float(information[1])
        if available_capacity:
            if maximum_weight_limit >= weight:
                available_capacity -= 1
                if type_of_pet not in information_gather:
                    information_gather[type_of_pet] = 0
                information_gather[type_of_pet] += 1
            pets_counter += 1
        if not available_capacity:
            break
    if pets_counter == len(pet_information):
        result.append(f"All pets are accommodated! Available capacity: {available_capacity}.")
    else:
        result.append("You did not manage to accommodate all pets!")
    result.append("Accommodated pets:")
    for pet, weight in sorted(information_gather.items(), key=lambda x: x[0]):
        result.append(f"{pet}: {weight}")
    return '\n'.join(result)


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))

print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))

print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))
