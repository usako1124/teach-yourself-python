print('abs123'.isalnum()) # True
print('abs++'.isalnum()) # False
print('abcde'.isalpha()) # True
print('abc123'.isalpha()) # False
print('abc'.isascii()) # True
print('あいう'.isascii()) # False
print('100'.isdecimal()) # True
print('0x64'.isdecimal()) # False
print('1234'.isdigit()) # True
print('1234.56'.isdigit()) # False
print('百万'.isnumeric()) # True
print('million'.isnumeric()) # False
print('abc_123'.isidentifier()) # True
print('abc-123'.isidentifier()) # False
print('wings'.islower()) # True
print('Wings'.islower())  # False
print('WINGS'.isupper()) # True
print('Wings'.isupper())  # False
print('Wings Project'.istitle())  # True
print('WINGS Project'.istitle())  # False
print('Hello World'.isprintable())  # True
print('Hello\nWorld'.isprintable())  # False
print('   '.isspace())  # True
print('***'.isspace())  # False
