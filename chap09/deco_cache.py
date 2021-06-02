import random
from functools import lru_cache

# 0 〜 100 の乱数を取得

@lru_cache(maxsize=8)
def get_0to100():
    return random.randint(0, 100)

print(get_0to100())
print(get_0to100())
