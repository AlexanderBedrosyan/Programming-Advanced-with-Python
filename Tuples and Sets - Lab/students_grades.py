def new_dict(num):
    current_dict = {}
    for i in range(num):
        name, result = input().split(" ")
        if name not in current_dict:
            current_dict[name] = []
        current_dict[name].append(float(result))
    return current_dict


def final_result(dictionary):
    for key, values in dictionary.items():
        current_values = []
        for ch in values:
            current_ch = f"{ch:.2f}"
            current_values.append(str(current_ch))
        print(f"{key} -> {' '.join(current_values)} (avg: {sum(values) / len(values):.2f})")


num = int(input())
dict_result_names = new_dict(num)
final_result(dict_result_names)