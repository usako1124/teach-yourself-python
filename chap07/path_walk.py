import os

PATH = './chap07/doc'
for path, dirs, files in os.walk(PATH):
    print(path)
    print(dirs)
    print(files)
    print('-----')
