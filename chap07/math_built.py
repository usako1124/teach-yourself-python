import math

print(abs(-100))  # 100
print(math.ceil(1234.567))  # 1235
print(math.floor(1234.567))  # 1234
print(math.trunc(1234.567))  # 1234
print(round(1234.567, 2))  # 1234.57
print(math.pow(2, 4))  # 16
print(math.factorial(5))  # 120
print(math.sqrt(10000))  # 100.0
print(divmod(10, 3))  # (3, 1)
print(math.gcd(96, 36))  # 12
print(math.nan)  # nan
print(math.inf)  # inf

data = ['はくさい', 'ねぎ', 'レタス', 'ブロッコリー']
print(min(data, key = lambda n: len(n)))  # ねぎ
print(max(data, key = lambda n: len(n)))  # ブロッコリー

print(math.pi)  # 3.141592653589793
print(round(math.cos(math.pi / 180 * 60), 1))  # 0.5
print(round(math.sin(math.pi / 180 * 30), 1))  # 0.5
print(round(math.tan(math.pi / 180 * 45), 1))  # 1
print(math.e)  # 2.718281828459045
print(math.exp(2))  # 7.38905609893065
print(math.log10(100))  # 2.0
print(math.frexp(0.0123))  # (0.7872, -6)
print(math.modf(3.14159))  # (0.14158999999999988, 3.0)
print(math.copysign(3.14159, -3.0))  # -3.14159
