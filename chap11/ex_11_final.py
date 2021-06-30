# [1]
# ◯ → ×
# ×
# ×
# ◯
# ×

# [2]
# class SingletonMeta(type):
#     def __init__(cls, name, bases, disc, **kwargs):
#         cls.__instance = None

#     def __call__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__call__(*args, **kwargs)
#         return cls.__instance

# class MySingleton(metaclass=SingletonMeta):
#     pass

# if __name__ == '__main__':
#     c1 = MySingleton()
#     c2 = MySingleton()
#     print(c1 is c2)

# [3]
# ①
import dataclasses
class Person:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f'Person:{self.name}'

# ②
class MyAppError(Exception):
    pass

# ③
@dataclasses.dataclass(frozen=True)
class Book():
    title: str
    price: int

# ④
for f in dataclasses.fields(Book):
    print(f)

# ⑤
try:
    raise KeyError
except KeyError:
    raise
except TypeError:
    raise
finally:
    print('終了しました')
