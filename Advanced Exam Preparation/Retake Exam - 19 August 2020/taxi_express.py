from collections import deque


def final(list_of_customers, total_time):
    if not list_of_customers:
        print(f"All customers were driven to their destinations\nTotal time: {total_time} minutes")
    else:
        print(f"Not all customers were driven to their destinations\nCustomers left: {', '.join(str(ch) for ch in list_of_customers)}")


list_of_customers = deque(int(ch) for ch in input().split(', '))
your_taxis = deque(int(ch) for ch in input().split(', '))
total_time = 0

while list_of_customers and your_taxis:
    first_customer = list_of_customers.popleft()
    last_taxi = your_taxis.pop()

    if first_customer <= last_taxi:
        total_time += first_customer
        continue
    else:
        list_of_customers.appendleft(first_customer)

final(list_of_customers, total_time)