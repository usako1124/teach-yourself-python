class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Coordinate 同士の加算
    def __add__(self, other):
        # 右オペランドの型によって処理を分岐
        if isinstance(other, Coordinate):
            # Coordinate 同士の加算
            return Coordinate(
                self.x + other.x,
                self.y + other.y
            )
        elif isinstance(other, int):
            # Coordinate + int の加算
            return Coordinate(
                self.x + other,
                self.y
            )
        else:
            # それ以外の型は不可
            raise TypeError('type must be Coordinate or int')

    def __str__(self):
        return f'({self.x}, {self.y})'

if __name__ == '__main__':
    # Coordinate 同士を加算
    c1 = Coordinate(10, 20)
    c2 = Coordinate(15, 35)
    print(c1 + 10)
    print(c1 + c2)
    print(c1 + 'hoge')
