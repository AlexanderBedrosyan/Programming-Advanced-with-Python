# Solution 1
print(sum(int(ch) for ch in open('numbers_text.txt', 'r')))

# Solution 2
def sum_of_numbers(file_name):
    with open(file_name, "r") as file:
        return sum(int(x) for x in file)


print(sum_of_numbers('numbers_text.txt'))