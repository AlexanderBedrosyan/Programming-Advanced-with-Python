from collections import deque


def is_fresh(current_egg):
    return current_egg > 0


def is_bad_luck_egg(current_egg):
    return current_egg != 13


def result_in_box_size(current_result):
    return result <= 50


eggs = deque(int(ch) for ch in input().split(', '))
papers = deque(int(ch) for ch in input().split(', '))
eggs_in_the_box = 0

while eggs and papers:
    first_egg = eggs.popleft()
    if not is_fresh(first_egg):
        continue
    if not is_bad_luck_egg(first_egg):
        papers[0], papers[-1] = papers[-1], papers[0]
        continue

    last_piece_of_paper = papers.pop()
    result = last_piece_of_paper + first_egg

    if result_in_box_size(result):
        eggs_in_the_box += 1

if eggs_in_the_box:
    print(f"Great! You filled {eggs_in_the_box} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(str(ch) for ch in eggs)}")
if papers:
    print(f"Pieces of paper left: {', '.join(str(ch) for ch in papers)}")