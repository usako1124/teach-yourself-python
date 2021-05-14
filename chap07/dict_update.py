d1 = {'apple': 'りんご', 'orange': 'みかん'}
d2 = {'melon': 'メロン', 'orange': '蜜柑'}

d1.update(d2)
print(d1)  # {'apple': 'りんご', 'orange': '蜜柑', 'melon': 'メロン'}

d1.update(strawberry='いちご', watermelon='すいか')
print(d1)  # {'apple': 'りんご', 'orange': '蜜柑', 'melon': 'メロン', 'strawberry': 'いちご', 'watermelon': 'すいか'}

d1.update([('pear', 'なし'), ('grape', 'ぶどう')])
print(d1)  # {'apple': 'りんご', 'orange': '蜜柑', 'melon': 'メロン', 'strawberry': 'いちご', 'watermelon': 'すいか', 'pear': 'なし', 'grape': 'ぶどう'}
