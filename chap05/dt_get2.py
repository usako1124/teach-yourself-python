import datetime

dt = datetime.datetime.now(datetime.timezone.utc)
print(dt)  # 2021-05-05 06:25:xx.xxxxxx
print(dt.date())  # 2021-05-05
print(dt.time())  # 06:25:xx.xxxxxx
print(dt.timetz())  # 06:25:xx.xxxxxx+00:00
print(dt.timestamp())  # xxxxxx
print(dt.toordinal())  # xxxxxx
print(dt.weekday())  # 2
print(dt.isoweekday())  # 3
print(dt.isocalendar())  # (2021, xx, 3)
