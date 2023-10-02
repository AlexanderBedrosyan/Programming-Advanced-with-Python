def even_odd_filter(**kwargs):
    new_dict = {}
    for key, values in kwargs.items():
        if key == "odd":
            new_dict[key] = [ch for ch in values if ch % 2 != 0]
        else:
            new_dict[key] = [ch for ch in values if ch % 2 == 0]
    sorted_dict = dict(sorted(new_dict.items(), key=lambda x: (len(x[1]), x[0]), reverse=True))
    return sorted_dict


print(even_odd_filter(odd=[1, 2, 3, 4, 10, 5], even=[3, 4, 5, 7, 10, 2, 5, 5, 2],))
