# [1]
# ① 初期化メソッド
# ② インスタンス変数 ※
# ③ クラスメソッド
# ④ @classmethod
# ⑤ cls ※
# ⑥ is-a
# ⑦ オーバーライド
# ⑧ super
# ⑨ 委譲
# ⑩ has-a

# [2]
# ◯ ※
# ×：ミックスイン
# ×：@property デコレーター
# ×
# ×

# [3]
# from abc import abstractmethod, ABC

# class Figure(ABC): # ABC が継承されてない
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
    
#     @abstractmethod  # @abstract ではなく @abstractmethod
#     def get_area(self):
#         pass

# class Triangle(Figure): # extend ではなく()
#     def get_area(self):
#         return self.width * self.height / 2

# class Square(Figure):
#     def get_area(self):
#         return self.width * self.height

# if __name__ == '__main__':
#     figs = [
#         Triangle(10, 15),
#         Square(10, 15),
#         Triangle(5, 1)
#     ]

#     for fig in figs:
#         if isinstance(fig, Figure):  # issubclass ではなく isinstance
#             print(f'{fig. __class__}:{fig.get_area()}')  # __name__ ではなく __class__


class Hamster:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def show(self, fmt):
        print(fmt.format(self.__name))
    
if __name__ == '__main__':
    h = Hamster('のどか')
    h.show('わたしの名前は{0}です')
