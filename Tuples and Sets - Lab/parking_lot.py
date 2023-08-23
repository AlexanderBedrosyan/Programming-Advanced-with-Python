def tuples_func(num):
    current_in_tuple = []
    current_out_tuple = []
    for i in range(num):
        position, car_number = input().split(", ")
        if position == "IN":
            if car_number not in current_in_tuple:
                current_in_tuple.append(car_number)
        else:
            current_out_tuple.append(car_number)
    return current_in_tuple, current_out_tuple


def final_result(in_tuple, out_typle):
    for ch in out_typle:
        if ch in in_tuple:
            in_tuple.remove(ch)
    if in_tuple:
        print('\n'.join(in_tuple))
    else:
        print("Parking Lot is Empty")


num = int(input())
in_tuple, out_tuple = tuples_func(num)
final_result(in_tuple, out_tuple)
