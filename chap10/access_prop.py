class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # name のゲッター
    @property
    def name(self):
        return self.__name

    # age のゲッター
    @property
    def age(self):
        return self.__age

    # name のセッター
    @name.setter
    def name(self, value):
        self.__name = value

    # name のセッター
    @age.setter
    def age(self, value):
        if value <= 0:
            raise ValueError('age は整数で設定します')
        self.__age = value

    def show(self):
        print(f'わたしの名前は{self.get_name}、{self.get_age}歳です！')

if __name__ == '__main__':
    p = Person('山田太郎', 15)
    p.name = '鈴木次郎'
    p.age = 35
    print(p.name)
    print(p.age)
