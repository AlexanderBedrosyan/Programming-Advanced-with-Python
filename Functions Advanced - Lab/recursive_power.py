def recursive_power(*args):
    if args[1] == 0:
        return 1
    else:
        return args[0] * recursive_power(args[0], args[1] - 1)


print(recursive_power(2, 10))
