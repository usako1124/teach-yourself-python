d = {'apple': 'りんご', 'orange': 'みかん', 'melon': 'メロン'}
d['apple'] = '林檎'
d['strawberry'] = 'いちご'
print(d.setdefault('apple', '◯'))  # '林檎'
print(d.setdefault('watermelon', '◯'))  # '◯'

print(d)  # {'apple': '林檎', 'orange': 'みかん', 'melon': 'メロン', 'strawberry': 'いちご', 'watermelon': '◯'}
