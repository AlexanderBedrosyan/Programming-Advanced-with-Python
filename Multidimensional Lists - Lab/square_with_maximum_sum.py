matrix = []
rows, columns = (int(ch) for ch in input().split(", "))

for _ in range(rows):
    matrix.append([int(ch) for ch in input().split(", ")])

biggest_sum = 0
final_list = []

for row in range(rows):
    for column in range(columns):
        current_list = []
        if row + 1 <= (rows - 1) and column + 1 <= (columns - 1):
            current_list.append([matrix[row][column], matrix[row][column + 1]])
            current_list.append([matrix[row + 1][column], matrix[row + 1][column + 1]])
            if (sum(current_list[0]) + sum(current_list[1])) > biggest_sum:
                biggest_sum = (sum(current_list[0]) + sum(current_list[1]))
                final_list = []
                for ch in current_list:
                    final_list.append(ch)

for i in range(len(final_list)):
    print(*final_list[i])
print(biggest_sum)
