class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def show(self):
        print(f'わたしの名前は{self.name}、{self.age}歳です！')

if __name__ == '__main__':
    p = Person('山田太郎', 15)
    print(p.age)