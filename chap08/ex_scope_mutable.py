def increment(num):
    num += 10
    return num

def param_update(data):
    data[0] = 100
    return data

num = 100
data = [10, 20, 30]

print(increment(num))  # 110
print(num)  # 100
print(param_update(data))  # [100, 20, 30]
print(data)  # [100, 20, 30]
