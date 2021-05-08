data = ['高江', '青木', '片渕']
data.append('土井')
print(data)  # ['高江', '青木', '片渕', '土井']
data.insert(0, '小林')
data.insert(-1, '吉川')
print(data)  # ['小林', '高江', '青木', '片渕', '吉川', '土井']
print(data.pop(0))  # '小林'
print(data.pop())  # '土井'
print(data)  # ['高江', '青木', '片渕', '吉川']
