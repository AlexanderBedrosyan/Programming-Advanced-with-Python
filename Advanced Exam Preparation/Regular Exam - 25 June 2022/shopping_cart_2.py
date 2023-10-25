def shopping_cart(*args):
    def is_limit(product, current_added_counter):
        products_limit = {
            'Soup': 3,
            'Pizza': 4,
            'Dessert': 2,
        }
        return products_limit[product] > current_added_counter

    def is_valid(element):
        return element != 'Stop'

    meals_counter = {
        'Pizza': [],
        'Dessert': [],
        'Soup': []
    }

    for elements in args:
        if not is_valid(elements):
            break
        type_of_product, product = elements[0], elements[1]
        if not is_limit(type_of_product, len(meals_counter[type_of_product])):
            continue
        if product in meals_counter[type_of_product]:
            continue
        meals_counter[type_of_product].append(product)

    final_result = []
    sorted_dict = dict(sorted(meals_counter.items(), key=lambda x: (-len(x[1]), x[0])))
    is_there_any_products = False
    for meal, current_product in sorted_dict.items():
        final_result.append(f'{meal}:')
        if not current_product:
            continue
        for ch in sorted(current_product):
            final_result.append(f" - {ch}")
        is_there_any_products = True
    if not is_there_any_products:
        final_result = ['No products in the cart!']
    return '\n'.join(final_result)


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'ham'),
#     'Stop',
# ))
#
# print(shopping_cart(
#     'Stop',
#     ('Pizza', 'ham'),
#     ('Pizza', 'mushrooms'),
# ))
