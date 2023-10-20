from collections import deque

pizza_orders = deque(int(ch) for ch in input().split(', '))
employees_capacities = deque(int(ch) for ch in input().split(', '))
total_pizza_completed = 0

while pizza_orders and employees_capacities:
    first_order = pizza_orders.popleft()
    if first_order > 10 or first_order <= 0:
        continue
    last_employee = employees_capacities.pop()
    if last_employee <= 0:
        pizza_orders.appendleft(first_order)
        continue

    if first_order <= last_employee:
        total_pizza_completed += first_order
        continue

    first_order -= last_employee
    total_pizza_completed += last_employee
    pizza_orders.appendleft(first_order)

if pizza_orders:
    print(f"Not all orders are completed.")
    print(f"Orders left: {', '.join(str(ch) for ch in pizza_orders)}")
else:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizza_completed}")
    print(f"Employees: {', '.join(str(ch) for ch in employees_capacities)}")
