data = 'グローバル'

def check_scope():
    global data
    data = 'ローカル'
    return data

print(check_scope())  # ローカル
print(data) # ローカル