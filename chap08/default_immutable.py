def my_func(value, list=[]):
    list.append(value)
    return list

print(my_func(13))  # [13]
print(my_func(108))  # [13, 108]
