data = ['い', 'ろ', 'は', 'に', 'ほ', 'へ', 'と', 'い', 'ろ']

print(data.index('い'))  # 0
print(data.index('い', 4))  # 7
# print(data.index('い', 4, 7))  # エラー
print(data.index('い', -4, -1))  # 7
