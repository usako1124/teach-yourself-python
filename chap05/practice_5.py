# 1
title = 'となりのきゃくはよくきゃくくうきゃくだ'
print(title.rfind('きゃく'))

# 2
pref = '千葉'
num = 17.256
print(f'{pref}の気温は{num:.2f}度です。')  # ?

# 3
title = '彼女の名前は花子です。'
print(title.replace('彼女', '妻'))

# 4
import datetime
dt = datetime.datetime.now()
dt = dt + datetime.timedelta(days=5, hours=6)
print(dt)

# 5
import calendar
print(calendar.month(2020, 10, 5))