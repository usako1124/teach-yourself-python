sets1 = {15, 25, 37, 20}
sets2 = {10, 13, 32}
sets3 = {25, 37}

print(10 in sets1)  # False
print(10 not in sets1)  # True

print(sets3.issubset(sets1))  # True
print(sets3 <= sets1)  # True
print(sets1.issuperset(sets3)) # True
print(sets1 >= sets3) # True
print(sets1.isdisjoint(sets2))  # True
print(sets1.isdisjoint(sets3))  # False
