import asyncio
import time

async def heavy_process(name, sec):  # async と await が逆
    print(f'start {name}')  # r じゃなくてf
    await asyncio.sleep(sec)  # time じゃなくて asyncio
    print(f'end {name}')
    return f'{name}/{sec}'

start = time.time()
result = asyncio.get_event_loop().run_until_complete(  # .get_event_loop() が必要
    asyncio.gather(  # run じゃなくて gather
        heavy_process('hoge', 2),
        heavy_process('bar', 5),
        heavy_process('piyo', 1),
        heavy_process('spam', 3)
    )
)
end = time.time()
print(result)
print(f'Process Time: {end - start}')
