# リストから順にファイルパスを取り出して読み込みは委譲
def read_files(*files):
    for file in files:
        yield from read_lines(file)

# ファイル読み込みを担うサブジェネレーター
def read_lines(path):
    with open(path, 'r', encoding='UTF-8') as file:
        # 行単位にテキストを取得
        for line in file:
            yield line.rstrip('\n')

# sample1〜3.dat の内容を順に列挙
for line in read_files(
    './chap09/sample1.dat', './chap09/sample2.dat', './chap09/sample3.dat'):
    print(line)
