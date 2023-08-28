matrix = []
num = int(input())
final_result = []

for _ in range(num):
    matrix.append([int(ch) for ch in input().split(", ")])

for ch in range(len(matrix)):
    for integer in matrix[ch]:
        final_result.append(integer)

print(final_result)
