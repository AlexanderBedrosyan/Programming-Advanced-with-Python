from collections import deque

bowls_of_ramen = deque(int(ch) for ch in input().split(', '))
customers = deque(int(ch) for ch in input().split(', '))

while bowls_of_ramen and customers:
    the_last_bowls = bowls_of_ramen.pop()
    first_customer = customers.popleft()

    if the_last_bowls == first_customer:
        continue

    if the_last_bowls > first_customer:
        the_last_bowls -= first_customer
        bowls_of_ramen.append(the_last_bowls)
        continue

    if first_customer > the_last_bowls:
        first_customer -= the_last_bowls
        customers.appendleft(first_customer)
        continue

if not customers:
    print("Great job! You served all the customers.")
    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join(str(ch) for ch in bowls_of_ramen)}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(ch) for ch in customers)}")