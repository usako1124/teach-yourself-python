print(all([False, True, False]))  # False
print(any([False, True, False]))  # True
print(not any([False, True, False]))  # False

print(any(['あいう', '', '']))  # True
print(any(['', '', '']))  # False

print(all((True, True, False)))  # False

data = ['さざんか', 'ほうせんか', 'バラ', 'サクラ']
print(any([len(str) > 4 for str in data]))  # True
