class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    # 氏・名共に等しければ同値とする
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.firstname == other.firstname and \
                self.lastname == other.lastname

        return False

if __name__ == '__main__':
    p1 = Person('太郎', '山田')
    p2 = Person('次郎', '鈴木')
    p3 = Person('太郎', '山田')

    print(p1 == p2)
    print(p1 == p3)
