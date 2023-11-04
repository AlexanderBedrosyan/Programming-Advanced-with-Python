def shop_from_grocery_list(budget, *needed_products):
    list_of_needed_products = needed_products[0]
    products_prices = needed_products[1::]
    for charts in products_prices:
        product = charts[0]
        price = float(charts[1])
        if product in list_of_needed_products:
            if budget >= price:
                budget -= price
                list_of_needed_products.remove(product)
            else:
                break
    if len(list_of_needed_products) == 0:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(list_of_needed_products)}."

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))





