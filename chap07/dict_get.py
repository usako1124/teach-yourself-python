d = {'apple': 'りんご', 'orange': 'みかん', 'melon': 'メロン'}
# print(d['pear']) # Error
print(d.get('pear', '×'))  # ×
print(d.pop('melon', '×'))  # 'メロン'
print(d.popitem())  # ('orange', 'みかん')
print(d)  # {'apple': 'りんご'}
