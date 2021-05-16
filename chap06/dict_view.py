d = {'apple': 'りんご', 'orange': 'みかん', 'melon': 'メロン'}

# 項目を列挙
for item in d.items():
    print(item)
# ('apple', 'りんご')
# ('orange', 'みかん')
# ('melon', 'メロン')

for key, value in d.items():
    print(key, ':', value)
# apple : りんご
# orange : みかん
# melon : メロン

# キーを列挙
for key in d.keys():
    print(key)
# apple
# orange
# melon

# 値を列挙
for value in d.values():
    print(value)
# りんご
# みかん
# メロン
