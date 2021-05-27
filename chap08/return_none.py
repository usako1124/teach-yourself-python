def get_value(map, key):
    if key in map:
        return map[key]
    else:
        return None

obj = {'apple': '林檎'}
print(get_value(obj, 'aaa'))
