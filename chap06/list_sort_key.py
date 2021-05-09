data = ['さくら', 'バラ', 'チューリップ', 'コスモス']

data.sort(key=lambda x: len(x))
print(data)  # ['バラ', 'さくら', 'コスモス', 'チューリップ']
