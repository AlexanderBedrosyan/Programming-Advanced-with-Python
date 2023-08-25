def finding_the_longest_intersection(num):
    longest_intersection_list = [[]]

    for _ in range(num):
        split_one, split_two = input().split("-")
        first_num_split_one, second_num_split_one = split_one.split(",")
        first_num_split_two, second_num_split_two = split_two.split(",")
        open_number = 0
        closed_number = 0
        if int(first_num_split_one) > int(first_num_split_two):
            open_number = int(first_num_split_one)
        else:
            open_number = int(first_num_split_two)

        if int(second_num_split_one) > int(second_num_split_two):
            closed_number = int(second_num_split_two)
        else:
            closed_number = int(second_num_split_one)

        current_list = []

        for i in range(open_number, closed_number + 1):
            current_list.append(i)

        if len(longest_intersection_list[0]) < len(current_list):
            longest_intersection_list[0] = current_list

    print(f"Longest intersection is {longest_intersection_list[0]} with length {len(longest_intersection_list[0])}")


num = int(input())

finding_the_longest_intersection(num)