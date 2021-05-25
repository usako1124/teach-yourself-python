print(bool(''))  # False
print(bool(150))  # True

dec_num = int('10')
print(dec_num)  # 10
print(type(dec_num))  # <class 'int'>

# エラー
# i_num = int('1.414')
# print(i_num)
# print(type(i_num))

hex_num = int('0x10', 16)
print(hex_num)  # 16
print(type(hex_num))  # <class 'int'>

f_num = float('1.414e-5')
print(f_num)  # 1.414e-5
print(type(f_num))  # <class 'float'>

str_v = str(1.014)
print(str_v)  # 1.014
print(type(str_v))  # <class 'str'>
