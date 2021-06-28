class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    # インスタンス変数の内容を出力
    def show(self):
        print(f'わたしの名前は{self.lastname}{self.firstname}です！')

class PersonList:
    # Person クラスのリストを格納するための変数を準備
    def __init__(self):
        self.data= []
    
    def add(self, person):
        self.data.append(person)

if __name__ == '__main__':
    # PersonList に Person オブジェクトを格納
    pl = PersonList()
    pl.add(Person('太郎', '山田'))
    pl.add(Person('奈美', '掛谷'))
    pl.add(Person('悟助', '田中'))

    # PersonList の内容を順に処理し、その show メソッドを実行
    for p in pl.data:
        p.show()
