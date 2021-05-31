# 高階関数 walk_list を定義
def walk_list(data, func):
    # リストの内容を順に処理
    for key, value in enumerate(data):
        func(value, key)

result = 0  # 結果値を格納するためのグローバル変数
def show_item(value, key):
    global result
    result += value

data = [105, 53, 27, 87, 233]

walk_list(data, show_item)
print(result)  # 505
