# [1]
# ① 基底クラス
# ② 派生クラス
# ③ (Person)

# [2]
class MyClass:
    def __init__(self, kind, name):
        self.kind = kind
        self.name = name

    def show(self):
        return f'ペットの{self.kind}の名前は、{self.name}です。'

class MySubClass(MyClass):
    def show(self):
        return f'[{super().show()}]'

if __name__ == '__main__':
    p = MySubClass('犬', 'チャコぎん')
    print(p.show())
