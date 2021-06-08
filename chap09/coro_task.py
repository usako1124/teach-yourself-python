import time
import asyncio

# ダミーの重い処理
async def heavy_process(name, sec):
    print(f'start {name}')
    await asyncio.sleep(sec)
    print(f'end {name}')
    return f'{name}/{sec}'

# 非同期処理のエントリーポイント
async def main():
    print(await heavy_process('hoge', 2))
    print(await heavy_process('bar', 5))
    print(await heavy_process('piyo', 1))

start = time.time()
loop = asyncio.get_event_loop()
asyncio.run(main())
end = time.time()
print(f'Process Time: {end - start}')
