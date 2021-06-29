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
        self.data = []

    def __iter__(self):
        return iter(self.data)

    def add(self, person):
        self.data.append(person)

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def add(self, person):
        self.data.append(person)

if __name__ == '__main__':
    pl = PersonList()
    pl.add(Person('太郎', '山田'))
    pl.add(Person('奈美', '掛谷'))
    pl.add(Person('悟助', '田中'))

    pl[1] = Person('哲也', '佐藤')
    print(pl[1].firstname)
