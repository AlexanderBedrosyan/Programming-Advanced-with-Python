def age_assignment(*args, **kwargs):
    final_dict = {}
    var = ''
    for ch in args:
        first_letter = ch[0]
        for keys, values in kwargs.items():
            if first_letter == keys:
                final_dict[ch] = values
    for key, value in sorted(final_dict.items(), key=lambda x: x[0]):
        var += f"{key} is {value} years old." + "\n"

    return var


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
