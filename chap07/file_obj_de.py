import pickle

with open('./chap07/book.bin', 'rb') as file:
    b = pickle.load(file)
    print(b.title)