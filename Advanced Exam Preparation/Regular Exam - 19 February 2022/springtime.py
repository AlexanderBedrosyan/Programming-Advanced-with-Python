def start_spring(**kwargs):
    spring_time_info = {}

    for name, type_of_name in kwargs.items():
        if type_of_name not in spring_time_info:
            spring_time_info[type_of_name] = []
        if name not in spring_time_info[type_of_name]:
            spring_time_info[type_of_name].append(name)

    for type_of_name, list_of_names in spring_time_info.items():
        new_list = sorted(list_of_names, key=lambda x: x, reverse=False)
        spring_time_info[type_of_name] = new_list

    sorted_info = dict(sorted(spring_time_info.items(), key=lambda x: (-len(x[1]), x[0])))

    final_result = []

    for key, value in sorted_info.items():
        final_result.append(f"{key}:")
        for element in value:
            final_result.append(f"-{element}")
    return '\n'.join(final_result)


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
