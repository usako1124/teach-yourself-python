import collections

data = ['太郎', '花子', '次郎', '太郎', '太郎', '太郎', '花子']
result = collections.defaultdict(int)

for key in data:
    result[key] += 1

print(result)  # defaultdict(<class 'int'>, {'太郎': 4, '花子': 2, '次郎': 1})
