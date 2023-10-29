from collections import deque

six_seats = input().split(", ")
free_seats = {ch: 0 for ch in six_seats}
first_sequence = deque(int(ch) for ch in input().split(", "))
second_sequence = deque(int(ch) for ch in input().split(", "))

rotations_counter = 0
seat_matches = []

while rotations_counter != 10:
    rotations_counter += 1
    first_number = first_sequence.popleft()
    second_number = second_sequence.pop()
    letter_needed = chr(first_number + second_number)
    both_seats_for_check = [f"{first_number}{letter_needed}", f"{second_number}{letter_needed}"]
    condition = False

    for seat in both_seats_for_check:
        if seat in free_seats:
            if free_seats[seat] == 0:
                seat_matches.append(seat)
                if len(seat_matches) == 3:
                    print(f"Seat matches: {', '.join(seat_matches)}\nRotations count: {rotations_counter}")
                    exit()
                free_seats[seat] = 1
                condition = True
                break
            else:
                condition = True
                break

    if not condition:
        first_sequence.append(first_number)
        second_sequence.appendleft(second_number)

print(f"Seat matches: {', '.join(seat_matches)}\nRotations count: {rotations_counter}")
