import math

# 素数を求めるジェネレーター
def get_primes():
    num = 2  # 素数の開始値
    # 2から順に素数判定し、素数の場合にだけ yield （無限ループ）
    while True:
        if is_prime(num):
            yield num
        num += 1

def is_prime(value):
    result = True
    # 2 〜sqrt(value)で、value を割り切れる（=余りが0）ものがあるか
    for i in range(2, math.floor(math.sqrt(value)) + 1):
        if value % i == 0:
            result = False  # 割り切れるものがあれば素数でない
            break
    return result

# 素数を順に出力
for prime in get_primes():
    print(prime)
    # 素数が100を超えたところで終了
    if prime > 100:
        break