def average(*args):
    result = 0
    for value in args:
        result += value
    return result / len(args)

print(average(10, 30, 200))
