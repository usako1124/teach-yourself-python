import datetime

dt = datetime.datetime.now(datetime.timezone.utc)
print(dt)
print(dt.year)  # 2021
print(dt.month)  # 5
print(dt.day)  # 5
print(dt.hour)  # 6
print(dt.minute)  # 17
print(dt.second)  # その時によって変わる
print(dt.microsecond)  # その時によって変わる
print(dt.tzinfo)  # UTC