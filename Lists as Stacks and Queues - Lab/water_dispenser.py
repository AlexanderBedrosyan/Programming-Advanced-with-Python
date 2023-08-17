from collections import deque


def add(list, person):
    list.append(person)
    return list


water = int(input())
list_people = deque()

while True:
    command = input()

    if command == "Start":
        while len(list_people) > 0:
            liters = input().split(" ")
            if len(liters) > 1:
                water += int(liters[1])
            else:
                if water >= int(liters[0]):
                    water -= int(liters[0])
                    person = list_people.popleft()
                    print(f"{person} got water")
                else:
                    person = list_people.popleft()
                    print(f"{person} must wait")
        break

    list_people = add(list_people, command)

print(f"{water} liters left")