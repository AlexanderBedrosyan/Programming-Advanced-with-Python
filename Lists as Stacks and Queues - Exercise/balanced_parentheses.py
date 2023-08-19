balance_list = []
parantheses = input()
pairs = ["{}", "()", "[]"]

for ch in parantheses:
    if ch == "{" or ch == "(" or ch == "[":
        balance_list.append(ch)
    else:
        if len(balance_list) > 0:
            opposite_ch = balance_list.pop()
            new_string = opposite_ch + ch
            if new_string in pairs:
                continue
            else:
                print("NO")
                exit()
        else:
            print("NO")
            exit()

if len(balance_list) == 0:
    print("YES")
