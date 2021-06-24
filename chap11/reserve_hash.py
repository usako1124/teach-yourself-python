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

    # ハッシュ値を演算
    def __hash__(self):
        return hash((self.firstname, self.lastname))

if __name__ == '__main__':
    p = Person('太郎', '山田')
    dic = {p: '男'}
    print(dic[p])