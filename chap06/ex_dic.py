d = {'cucumber': 'キュウリ', 'lettuce': 'レタス', 'spinach': 'ホウレンソウ'}
d['cucumber'] = '胡瓜'
d.pop('spinach')
d.setdefault('carrot', 'ニンジン')

for item in d.items():
    print(item)

# ('cucumber', '胡瓜')
# ('lettuce', 'レタス')
# ('carrot', 'ニンジン')
