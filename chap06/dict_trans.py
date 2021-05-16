d = {'apple': 'りんご', 'orange': 'みかん', 'melon': 'メロン'}
result = { value: key for key, value in d.items() }
print(result)  # { 'りんご': 'apple', 'みかん': 'orange', 'メロン': 'melon' }
