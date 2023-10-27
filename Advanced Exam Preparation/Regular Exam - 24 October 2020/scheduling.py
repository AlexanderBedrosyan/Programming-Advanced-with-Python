from collections import deque

jobs = deque(int(ch) for ch in input().split(', '))
index_of_the_job_needed = int(input())
needed_amount = jobs[index_of_the_job_needed]
total_amount = 0

for element in jobs:
    if needed_amount >= element:
        total_amount += element

print(total_amount)