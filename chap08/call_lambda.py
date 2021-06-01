# 高階関数 walk_list を定義
def walk_list(data, func):
    # リストの内容を順に処理
    for key, value in enumerate(data):
        func(value, key)

data = [105, 53, 27, 87, 233]

walk_list(data, lambda value, key: print(key, ':', value))

# 0 : 105
# 1 : 53
# 2 : 27
# 3 : 87
# 4 : 233
