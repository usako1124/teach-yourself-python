class MyStack(list):
    # list#append をもとに push メソッドを定義
    def push(self, elem):
        self.append(elem)

    # その他の不要なメソッドは無効化
    def insert(self):
        raise RuntimeError('Not Support')

if __name__ == '__main__':
    s = MyStack([10, 20, 30])
    s.push(40)
    print(s.pop())
    print(s)
    # s.insert(1, 50)