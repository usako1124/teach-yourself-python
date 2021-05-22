import datetime
import os

PATH = './chap07'
for f in os.listdir(PATH):
    p = os.path.join(PATH, f)

    print(p)
    print('フォルダ' if os.path.isdir(p) else 'ファイル')
    print(datetime.datetime.fromtimestamp(os.path.getatime(p)))
    print(os.path.getsize(p), 'byte')
    print('-----')
