data = 'グローバル'

def check_scope():
    data = 'ローカル'
    return data

print(check_scope())  # ローカル
print(data)  # グローバル