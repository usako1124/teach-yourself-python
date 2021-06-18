class Figure():
    # width、height を準備
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    # 面積を取得（中身はダミー）
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
    t = Triangle(10, 15)
    r = Reactangle(10, 15)

    print(t.get_area())
    print(r.get_area())
