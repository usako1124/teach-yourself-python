msg = 'にわにわにわにわとりがいる'

print(msg.find('にわ')) # 0
print(msg.find('にも')) # -1
print(msg.rfind('にわ'))  # 6
print(msg.find('にわ', 3))  # 4
print(msg.find('にわ', 3, 5))  # -1 なのが謎
print(msg.find('にわ', -7, -1))  # 6
