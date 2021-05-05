import datetime

dt = datetime.datetime(2019, 12, 4, 15, 35, 58, 469)
dt_p = dt + datetime.timedelta(days=15, hours=5)
dt_m = dt - datetime.timedelta(weeks=3)

print(dt)  # 2019-12-04 15:35:58.000469
print(dt_p)  # 2019-12-19 20:35:58.000469
print(dt_m)  # 2019-11-13 15:35:58.000469
