from abc import abstractmethod, ABC

class Figure(ABC):
    # width、height を準備
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @abstractmethod
    def get_area(self):
        return 0.0

class Triangle(Figure):
    # 三角形を求めるための get_area メソッドを定義
    def get_area(self):
        return self.width * self.height / 2

class Reactangle(Figure):
    # 四角形を求めるための get_area メソッドを定義
    def get_area(self):
        return self.width * self.height

if __name__ == '__main__':
    # Figure 派生クラスのリストを準備
    figs = [
        Triangle(10, 15),
        Reactangle(10, 15),
        Triangle(5, 1)
    ]

    # 配列 figs の内容を順番に処理
    for fig in figs:
        if isinstance(fig, Figure):
            print(f'{fig.__class__}：{fig.get_area()}')
