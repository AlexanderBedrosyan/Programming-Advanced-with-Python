from collections import deque

rows, columns = (int(ch) for ch in input().split(" "))
string_list = deque([ch for ch in input()])
matrix = []
count = 0

for row in range(rows):
    current_matrix = []
    for col in range(columns):
        current_matrix.append("")
    matrix.append(current_matrix)

for row in range(rows):
    count += 1
    for col in range(columns):
        if count % 2 != 0:
            ch = string_list.popleft()
            matrix[row][col] = ch
            string_list.append(ch)
        else:
            ch = string_list.popleft()
            matrix[row][columns - 1 - col] = ch
            string_list.append(ch)

for i in range(len(matrix)):
    print(''.join(matrix[i]))