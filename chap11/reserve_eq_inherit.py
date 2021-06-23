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


class BusinessPerson(Person):
    def __init__(self, firstname, lastname, title):
        super().__init__(firstname, lastname)
        # title を追加
        self.title = title

if __name__ == '__main__':
    p = Person('太郎', '山田')
    bp = BusinessPerson('太郎', '山田', '部長')
    print(p == bp)
    print(bp == p)

