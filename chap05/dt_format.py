import datetime
import locale

locale.setlocale(locale.LC_ALL, 'ja_JP.UTF-8')

dt = datetime.datetime(2019, 12, 4, 15, 35, 58, 469)
print(dt)
print(dt.strftime('%c'))  # 水 12/ 4 15:35:58 2019
print(dt.strftime('%x'))  # 2019/12/04
print(dt.strftime('%X'))  # 15時35分58秒
print(dt.strftime('%Y年 %m月 %d日（%a） %I時 %M分'))  # 2019年 12月 04日（水） 3時 35分
