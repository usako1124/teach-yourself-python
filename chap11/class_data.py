import dataclasses

@dataclasses.dataclass(frozen=True)
class Person:
    firstname: str
    lastname: str
    age: int = 0

def show(self):
    print(f'私の名前{self.lastname}{self.lastname}です！')

if __name__ == '__main__':
    p1 = Person('太郎', '山田', 58)
    p2 = Person('太郎', '山田', 58)
    print(p1)
    print(p1 == p2)

