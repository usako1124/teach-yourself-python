import re

ptn = re.compile(r'\d{2,4}-\d{2,4}-\d{4}')
with open('./chap07/sample.dat', 'r', encoding='UTF-8') as file:
    for line in file:
        results = ptn.finditer(line)
        for result in results:
            print(result.group())


print(abs(-12))
print(round(987.654, 2))

import os
for f in os.listdir('./chap07'):
    print(f)


import random
print(random.randint(0, 100))

ptn = re.compile(r'[/\\]')
result = ptn.split('txt')
print(result)
