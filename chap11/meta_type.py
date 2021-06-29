# クラス定義に関わるメソッド（関数）を準備
def init(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname

def show(self):
    print(f'わたしの名前は{self.lastname}{self.firstname}です！')

# Person クラスを定義
Person = type(
    'Person',
    (object,),
    {
        '__init__': init,
        'show': show
    }
)

if __name__ == '__main__':
    p = Person('太郎', '山田')
    p.show()