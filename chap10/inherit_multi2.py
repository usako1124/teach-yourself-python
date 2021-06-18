class TopA:
    def hoge(self):
        print('TopA')

class TopB:
    def hoge(self):
        print('TopB')

class MiddleA(TopA, TopB):
    def hoge(self):
        print('MiddleA')

class MiddleB(TopB, TopA):
    def hoge(self):
        print('MiddleB')

# MiddleA・Bクラスを多重継承
class Low(MiddleA, MiddleB):
    pass

if __name__ == '__main__':
    l = Low()
    l.hoge()
