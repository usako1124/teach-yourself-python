import re

msg = '10人のインディアン。\n1年性になったら'
ptn = re.compile(r'^\d*', re.MULTILINE)
results = ptn.findall(msg)
for result in results:
    print(result)

# 10
# 1
