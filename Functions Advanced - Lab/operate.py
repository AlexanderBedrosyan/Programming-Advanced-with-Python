def operate(x, *args):
    if x == "+":
        number = 0
        for ch in args:
            number += ch
        return number
    elif x == "-":
        number = 0
        for i in range(len(args)):
            if i == 0:
                number = args[i]
            else:
                number -= args[i]
        return number
    elif x == "*":
        number = 1
        for ch in args:
            # if ch == 0:
            #     number = 1
            # else:
            number *= ch
        return number
    elif x == "/":
        number = 1
        for i in range(len(args)):
            if i == 0:
                number = float(args[i])
            else:
                if args[i] == 0:
                    continue
                else:
                    number /= float(args[i])
        return number


print(operate("*", 3, 4))
