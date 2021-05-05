import datetime

dt1 = datetime.datetime(2019, 11, 30, 4, 46, 14, 123)
dt2 = datetime.datetime(2020, 12, 4, 15, 35, 58, 469)
delta = dt2 - dt1
print(delta)  # 370 days, 10:49:44.000346
print(delta.days)  # 370
print(delta.seconds)  # 38984
