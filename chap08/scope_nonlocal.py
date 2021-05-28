data = 'global'

def outer():
    data = 'outer'

    def inner():

        data = 'inner'
        return data

    print(inner())  # inner
    print(data)  # outer

outer()
print(data)  # global
