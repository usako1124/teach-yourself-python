data1 = ['いぬ', 'ねこ', 'たぬき']
print(','.join(data1))  # 'いぬ,ねこ,たぬき'
data2 = [10, 103, 18]
# print('\t'.join(data2)) # Error
print('\t'.join(str(i) for i in data2))  # '10\t103\t18'
