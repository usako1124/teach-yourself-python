import collections

# キュー操作（末尾から要素を追加し、先頭から取り出す）
data = collections.deque()
data.append(10)
data.append(15)
data.append(30)
print(data)  # deque([10, 15, 30])
print(data.popleft())  # 10
print(data)  # deque([15, 30])

# スタック操作（末尾から要素を追加し、末尾から取り出す）
data2 = collections.deque()
data2.append(10)
data2.append(15)
data2.append(30)
print(data2)  # deque([10 , 15, 30])
print(data2.pop())  # 30
print(data2)  # deque([10 , 15])
