def gen_com():
    while True:
        # 入力ボックス呼び出し
        n = yield input('名前を教えてください。')
        # send メソッドからの値をメッセージで生成
        yield f'こんにちは、{n}さん！'

gen = gen_com()
for name in gen:
    # ジェネレーターからの戻り値（入力値）を再送出
    res =  gen.send(name.upper())
    print(res)