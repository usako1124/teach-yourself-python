msg = 'example.com/index.html'

print(msg.partition('.'))  # ('example', '.', 'com/index.html')
print(msg.rpartition('.'))  # ('example.com/index', '.', 'html')
print(msg.partition('|'))  # ('example.com/index.html', '', '')
