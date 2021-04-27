data = ['さくら', 'うめ', 'ききょう', 'くちなし', 'ぼたん']

for name in data:
    # 要素が「×」の場合にループ
    if name == '×':
        break
    print(name)
else:
    print('正常終了しました。')
