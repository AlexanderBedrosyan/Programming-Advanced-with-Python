n = int(input())

stack = []

for i in range(n):
    command = [int(ch) for ch in input().split()]

    if len(command) == 2:
        stack.append(command[1])
    else:
        if len(stack) > 0:
            if command[0] == 2:
                if len(stack) == 1:
                    stack = []
                else:
                    stack.pop()
            elif command[0] == 3:
                print(max(stack))
            elif command[0] == 4:
                print(min(stack))

print(*stack[::-1], sep=", ")
