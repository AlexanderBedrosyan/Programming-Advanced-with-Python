from collections import deque


def print_the_result(current_dict):
    print(f"Congratulations, all tasks have been completed! Rubber ducks rewarded:")
    for rubber, counter in current_dict.items():
        print(f"{rubber}: {counter}")


def count_the_number_of_tasks(task_time, number_tasks, time_needed_rubber, current_dict):
    while len(task_time) > 0 and len(number_tasks) > 0:
        first_task_time = task_time.popleft()
        last_number_tasks = number_tasks.pop()
        time_needed = first_task_time * last_number_tasks
        flag = False
        for rubber, range_time in time_needed_rubber.items():
            if time_needed in range_time:
                flag = True
                current_dict[rubber] += 1
        if not flag:
            last_number_tasks -= 2
            number_tasks.append(last_number_tasks)
            task_time.append(first_task_time)
    print_the_result(current_dict)


time_consuming_per_single_task = deque([int(ch) for ch in input().split(" ")])
number_of_tasks = [int(ch) for ch in input().split(" ")]
rubber_needed_time = {"Darth Vader Ducky": range(0, 61), "Thor Ducky": range(61, 121),
                      "Big Blue Rubber Ducky": range(121, 181), "Small Yellow Rubber Ducky": range(181, 241)}
final_dict = {"Darth Vader Ducky": 0, "Thor Ducky": 0, "Big Blue Rubber Ducky": 0, "Small Yellow Rubber Ducky": 0}

count_the_number_of_tasks(time_consuming_per_single_task, number_of_tasks, rubber_needed_time, final_dict)
