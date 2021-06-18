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
    pass

class Reactangle(Figure):
    pass

if __name__ == '__main__':
    t = Triangle(10, 15)
    r = Reactangle(10, 15)

    print(t.get_area())
    print(r.get_area())
