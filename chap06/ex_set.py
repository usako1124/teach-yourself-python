sets1 = {2, 4, 8, 16, 32}
sets2 = {1, 10, 4 ,16}

print(sets1.union(sets2))  # {32, 1, 2, 4, 8, 10, 16}
sets3 = { str(i) for i in sets1 if i > 5 }
print(sets3)  # {32, 8, 16}