numbers = [nums.split() for nums in input().split("|")]

for ch in numbers[::-1]:
    [print(chart, end=" ") for chart in ch]