data1 = 'グローバル'

def check_scope():
    data2 = 'ローカル'
    return data1

print(check_scope())  # グローバル
print(data2)  # エラー