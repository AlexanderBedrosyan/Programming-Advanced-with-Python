text = list(input())
index = []

for i in range(len(text)):
    if text[i] == "(":
        index.append(i)
    if text[i] == ")":
        position = index.pop()
        print(''.join(text[position:(i + 1)]))
