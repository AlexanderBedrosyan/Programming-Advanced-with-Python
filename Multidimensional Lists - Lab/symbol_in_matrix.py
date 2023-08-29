matrix = []
rows = int(input())

for _ in range(rows):
    matrix.append([ch for ch in input()])

searching_symbol = input()
checker = False

for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        if searching_symbol == str(matrix[row][column]):
            print(f"({row}, {column})")
            checker = True
            exit()

if not checker:
    print(f"{searching_symbol} does not occur in the matrix")
