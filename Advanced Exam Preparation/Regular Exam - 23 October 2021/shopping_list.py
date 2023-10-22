def shopping_list(budget, **kwargs):
    return_result = []
    if budget < 100:
        return "You do not have enough budget."
    for product, information in kwargs.items():
        price = float(information[0])
        quantity = int(information[1])
        total_price = price * quantity
        if total_price <= budget:
            return_result.append(f"You bought {product} for {total_price:.2f} leva.")
            budget -= total_price
        if len(return_result) == 5:
            break
    return '\n'.join(return_result)
