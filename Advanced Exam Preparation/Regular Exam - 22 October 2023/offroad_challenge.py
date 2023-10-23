from collections import deque

initial_fuel = deque(int(ch) for ch in input().split(' '))
additional_consumption_index = deque(int(ch) for ch in input().split(' '))
amount_of_fuel_needed = deque(int(ch) for ch in input().split(' '))
altitude_counter = 0
reached_altitude = []

while initial_fuel and additional_consumption_index and amount_of_fuel_needed:
    last_fuel = initial_fuel.pop()
    first_index = additional_consumption_index.popleft()
    element_needed = amount_of_fuel_needed.popleft()
    result = last_fuel - first_index
    altitude_counter += 1

    if result < element_needed:
        print(f"John did not reach: Altitude {altitude_counter}")
        break

    reached_altitude.append(f"Altitude {altitude_counter}")
    print(f"John has reached: Altitude {altitude_counter}")

if 0 < len(reached_altitude) < 4:
    print("John failed to reach the top.")
    print(f"Reached altitudes: {', '.join(reached_altitude)}")

if len(reached_altitude) == 0:
    print("John failed to reach the top.\nJohn didn't reach any altitude.")

if len(reached_altitude) == 4:
    print("John has reached all the altitudes and managed to reach the top!")
