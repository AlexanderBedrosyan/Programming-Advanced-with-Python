def stock_availability(*args):
    inventory_list = args[0]
    command = args[1]
    if command == "delivery":
        boxes = args[2:]
        for box in boxes:
            inventory_list.append(box)
    if command == "sell":
        rest_parm = args[2:]
        if not rest_parm:
            inventory_list.pop(0)
        elif f'{rest_parm[0]}'.isdigit():
            for _ in range(int(rest_parm[0])):
                if inventory_list:
                    inventory_list.pop(0)
        else:
            for order in rest_parm:
                while order in inventory_list:
                    inventory_list.remove(order)
    return inventory_list


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
