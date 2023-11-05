from collections import deque


def list_manipulator(*args):
    current_queue = deque(args[0])
    command = args[2]
    if len(args) == 3:

        if args[1] == "remove":
            if command =="beginning":
                ch = current_queue.popleft()
            elif command == "end":
                ch = current_queue.pop()
        elif args[1] == "add":
            if command =="beginning":
                pass
            elif command == "end":
                pass
    elif len(args) > 3:
        current_list = args[3::]
        needed_sum = sum(current_list)
        if args[1] == "remove":
            if command == "beginning":
                for _ in range(needed_sum):
                    if len(current_queue) > 0:
                        ch = current_queue.popleft()
            elif command == "end":
                for _ in range(needed_sum):
                    if len(current_queue) > 0:
                        ch = current_queue.pop()
        elif args[1] == "add":
            if command == "beginning":
                for ch in current_list[::-1]:
                    current_queue.appendleft(ch)
            elif command == "end":
                for i in range(len(current_list)):
                    current_queue.append(current_list[i])
    final_list = []
    for ch in current_queue:
        final_list.append(ch)
    return final_list


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
