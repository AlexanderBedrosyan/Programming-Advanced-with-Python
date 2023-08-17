def new_client(list, client):
    list.append(client)
    return list


def paid(list):
    for ch in list:
        print(ch)


def end(list):
    print(f"{len(list)} people remaining.")


clients = []

while True:
    command = input()

    if command == "End":
        end(clients)
        break
    elif command == "Paid":
        paid(clients)
        clients = []
    else:
        clients = new_client(clients, command)
