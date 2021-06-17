class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def show(self):
        print(f'わたしの名前は{self.lastname}{self.firstname}です！')

# Person を継承した BusinessPerson クラスを定義
class BusinessPerson(Person):
    def work(self):
        print(f'{self.lastname}{self.firstname}は働いてるよ')

class HetareBusinessPerson(BusinessPerson):
    def work(self):
        super().work()
        print('ただし、ボチボチと')

if __name__ == '__main__':
    bp = HetareBusinessPerson('太郎', '山田')
    bp.work()
