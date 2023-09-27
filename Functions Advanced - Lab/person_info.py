def get_info(**args):
    return f"This is {args['name']} from {args['town']} and he is {args['age']} years old"


print(get_info(**{"name": "George", "town":"Sofia", "age": 20}))
