import requests

# 書籍情報を管理
class Book:
    def __init__(self, isbn, title, price):
        self.isbn = isbn
        self.title = title
        self.price = price

    # ISBN コード（isbn）をキーに書籍情報を取得
    @classmethod
    def get_by_isbn(cls, isbn):
        #＜ISBNコード＞.json を取得
        res = requests.get(f'http://usacode.xsrv.jp/study/python/{isbn}.json')
        print(res)
        bs = res.json()
        # 取得した書籍情報を元にインスタンスを作成
        return cls(bs['isbn'], bs['title'], bs['price'])

if __name__ == '__main__':
    b = Book.get_by_isbn('978-4-7981-5112-0')
    print(b.title)
