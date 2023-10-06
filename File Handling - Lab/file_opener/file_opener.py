# Solution 1
try:
    file = open('text.txt', 'r')
    print('File found')
except FileNotFoundError:
    print('File not found')

# Solution 2

try:
    with open('text.txt', 'r') as file:
        print('File found')
except FileNotFoundError:
    print('File not found')