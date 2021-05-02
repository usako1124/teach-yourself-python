msg = 'WINGSプロジェクト'

print('プロ' in msg) # True
print('プロ' not in msg) # False
print(msg.startswith('WINGS')) # True
print(msg.endswith('WINGS')) # False
print(not msg.startswith('WINGS')) # False
print(msg.startswith('WINGS', 1)) # False
print('プロ' in msg[6:]) # False
print('wings' in msg)  # False
print('wings' in msg.casefold())  # True
