def reservation_func(num):
    current_tuple = set()
    for _ in range(num):
        current_tuple.add(input())
    return current_tuple


def final_result(tuple):
    vip_guests = []
    guests = []
    while True:
        command = input()
        if command == "END":
            break

        if command in tuple:
            tuple.remove(command)

    for ch in tuple:
        if ch[0].isdigit():
            vip_guests.append(ch)
        else:
            guests.append(ch)

    print(f"{len(vip_guests) + len(guests)}")
    for ch in sorted(vip_guests):
        print(ch)
    for chart in sorted(guests):
        print(chart)


num = int(input())
reservation_tuple = reservation_func(num)
final_result(reservation_tuple)
