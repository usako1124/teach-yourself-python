import bisect

data = [108, 12, 9, 57, 63, 30]
data.sort()
print(data)  # [9, 12, 30, 57, 63, 108]
bisect.insort(data, 43)
print(data)  # [9, 12, 30, 43, 57, 63, 108]
