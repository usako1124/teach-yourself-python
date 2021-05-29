# arg 2, 3はキーワード引数であること
def my_func(arg, *, arg2=0, arg3=0):
    pass

my_func(1, 2, 3)  # Error