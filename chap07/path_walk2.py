import os

PATH = './chap07/doc'
for path, dirs, files in os.walk(PATH):
    for f in files:
        # 拡張子が .txt のものだけを列挙
        if f.endswith('.txt'):
            print(os.path.join(path, f))