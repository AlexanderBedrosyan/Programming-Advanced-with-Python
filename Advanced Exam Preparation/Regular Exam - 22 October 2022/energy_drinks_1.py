from collections import deque

MAX_CAFFEINIE_PER_NIGHT = 300
stamat_total_caffeine = 0

milligrams_of_caffeine = deque(int(ch) for ch in input().split(", "))
energy_drinks = deque(int(ch) for ch in input().split(", "))

while milligrams_of_caffeine and energy_drinks:
    last_milligram = milligrams_of_caffeine.pop()
    first_drink = energy_drinks.popleft()

    needed_caffeine = last_milligram * first_drink
    if (needed_caffeine + stamat_total_caffeine) <= MAX_CAFFEINIE_PER_NIGHT:
        stamat_total_caffeine += needed_caffeine
    else:
        energy_drinks.append(first_drink)
        if stamat_total_caffeine - 30 >= 0:
            stamat_total_caffeine -= 30
        else:
            stamat_total_caffeine = 0

if energy_drinks:
    print(f"Drinks left: {', '.join(str(ch) for ch in energy_drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {stamat_total_caffeine} mg caffeine.")
