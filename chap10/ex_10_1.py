class Pet:
    def __init__(self, kind, name):  # __new__ じゃなくて __init__
        self.kind = kind
        self.name = name

    def show(self):  # self が必要？
        print(f'わたしのペットは{self.kind}の{self.name}ちゃんです！')

if __name__ == '__main__':  # app じゃなくて main
    p = Pet('ハムスター', 'のどか')  # new いらない
    p.show()  # -> じゃなくて .