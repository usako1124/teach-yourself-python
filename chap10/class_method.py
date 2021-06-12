class Person:
    __slots__ = ['firstname', 'lastname', 'age']

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    # インスタンス変数の内容を出力
    def show(self):
        print(f'わたしの名前は{self.lastname}{self.firstname}です！')
