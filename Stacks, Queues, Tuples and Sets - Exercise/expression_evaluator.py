def sum_result(list, ch, count, result):
    for i in range(len(list)):
        if count == 0 and i == 0:
            result = list[i]
            continue
        if ch == "*":
            result *= list[i]
        elif ch == "+":
            result += list[i]
        elif ch == "-":
            result -= list[i]
        else:
            result //= list[i]

    return result



operators_list = ["*", "+", "-", "/"]
string_exrepssion = [ch for ch in input().split(" ")]
result = 0
current_list = []
count = 0

for ch in string_exrepssion:
    current_ch = ch
    if current_ch in operators_list:
        result = sum_result(current_list, current_ch, count, result)
        count += 1
        current_list = []
    else:
        current_list.append(int(current_ch))


print(result