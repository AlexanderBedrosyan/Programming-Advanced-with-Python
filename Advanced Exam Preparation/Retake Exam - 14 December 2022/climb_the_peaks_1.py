from collections import deque

quantities_of_daily_portions = deque(int(ch) for ch in input().split(", "))
stamina_quantities = deque(int(ch) for ch in input().split(", "))
peaks_difficulty = {"Vihren": 80, "Kutelo": 90, "Banski Suhodol": 100, "Polezhan": 60, "Kamenitza": 70}
conquered_mountain = []

while quantities_of_daily_portions and stamina_quantities and peaks_difficulty:
    current_result = quantities_of_daily_portions.pop() + stamina_quantities.popleft()

    for mountain, diff in peaks_difficulty.items():
        if current_result >= diff:
            conquered_mountain.append(mountain)
            peaks_difficulty.pop(mountain)
        break

if not peaks_difficulty:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK\nConquered peaks:")
    print(*conquered_mountain, sep="\n")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
    if conquered_mountain:
        print("Conquered peaks:")
        print(*conquered_mountain, sep="\n")
