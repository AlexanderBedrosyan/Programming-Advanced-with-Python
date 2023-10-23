from collections import deque

tools = deque(int(ch) for ch in input().split(' '))
substances = deque(int(ch) for ch in input().split(' '))
challenges = [int(ch) for ch in input().split(' ')]

while tools and substances and challenges:
    first_tool = tools.popleft()
    last_substances = substances.pop()
    result = first_tool * last_substances

    if result in challenges:
        challenges.remove(result)
        if not challenges:
            break
        continue

    first_tool += 1
    tools.append(first_tool)
    last_substances -= 1
    if last_substances > 0:
        substances.append(last_substances)

if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print(f"Tools: {', '.join(str(ch) for ch in tools)}")
if substances:
    print(f"Substances: {', '.join(str(ch) for ch in substances)}")
if challenges:
    print(f"Challenges: {', '.join(str(ch) for ch in challenges)}")