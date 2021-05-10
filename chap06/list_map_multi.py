data1 = [1, 3, 5]
data2 = [2, 7, 10]


result = map(lambda v1, v2: v1 * v2, data1, data2)
print(list(result))   # [2, 21, 50]
