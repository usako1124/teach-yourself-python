import dataclasses

@dataclasses.dataclass()
class Person:
    firstname: str
    lastname: str
    age: int = 0
    memos: list = dataclasses.field(default_factory=list)

if __name__ == '__main__':
    ms = ['married', 'AB']
    p = Person('太郎', '山田', 58, ms)
    # 初期化メソッドに渡したオブジェクトを変更
    ms.append('dog')
    print(p)
