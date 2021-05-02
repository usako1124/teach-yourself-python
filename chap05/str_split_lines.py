msg = '''\
こんにちは
こんばんは
さようなら
'''

print(msg.splitlines())  # ['こんにちは', 'こんばんは', 'さようなら']
print(msg.splitlines(True))  # ['こんにちは\n', 'こんばんは\n', 'さようなら\n']
