class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def show(self):
        print(f'わたしの名前は{self.lastname}{self.firstname}です！')

class Foreigner(Person):
    def __init__(self, firstname, middlename, lastname):
        # 基底クラスのコンストラクターを呼び出し
        super().__init__(firstname, lastname)
        # 独自の middlename を初期化
        self.middlename = middlename

    def show(self):
        print(f'わたしの名前は{self.lastname}.{self.middlename}.{self.firstname}です！')

if __name__ == '__main__':
    bp = Foreigner('太郎', 'ヨーダ', '山田')
    bp.show()
