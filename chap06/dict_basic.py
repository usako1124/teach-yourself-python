d1 = {'red': '赤', 'white': '白', 'yellow': '黄'}
print(d1)  # {'red': '赤', 'white': '白', 'yellow': '黄'}

d2 = {}
print(d2)  # {}

d3 = dict(red='赤', white='白', yellow='黄')
print(d3)  # {'red': '赤', 'white': '白', 'yellow': '黄'}

d4 = dict([('red', '赤'), ('white', '白'), ('yellow', '黄')])
print(d4)  # {'red': '赤', 'white': '白', 'yellow': '黄'}

d5 = dict({'red': '赤', 'white': '白', 'yellow': '黄'})
print(d5)  # {'red': '赤', 'white': '白', 'yellow': '黄'}

d6 = dict({'red': '赤', 'white': '白', 'yellow': '黄'}, white='しろ', black='黒')
print(d6)  # {'red': '赤', 'white': 'しろ', 'yellow': '黄', 'black': '黒'}

d7 = dict(zip(['red', 'white', 'yellow'], ['赤', '白', '黄']))
print(d7)  # {'red': '赤', 'white': '白', 'yellow': '黄'}
