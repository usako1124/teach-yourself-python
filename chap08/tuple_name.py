import collections

def get_max_min(*args):
    MaxMin = collections.namedtuple('MaxMin', ['max', 'min'])
    return MaxMin(max(args), min(args))

retult = get_max_min(15, 7.5, 108, -10)
print(retult.max)  # 108
print(retult.min)  # -10
print(retult[0])  # 108
