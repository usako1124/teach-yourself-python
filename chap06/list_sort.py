data1 = ['ぱんだ', 'うさぎ', 'こあら', 'とら']
data2 = [205, 13, 78, 50]
data3 = ['ぱんだ', 15, 'こあら']

data1.sort()
print(data1)  # ['うさぎ', 'こあら', 'とら', 'ぱんだ']
data2.sort()
print(data2)  # [13, 50, 78, 205]
# data3.sort()
print(data3)  # エラー
data1.sort(reverse=True)
print(data1)  # ['ぱんだ', 'とら', 'こあら', 'うさぎ']
