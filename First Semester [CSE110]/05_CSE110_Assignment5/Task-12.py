dict_1 = {'A': [1, 2, 3], 'b': ['1', '2'], "c": [4, 5, 6, 7]}
newlist = []
counter = 0
for val in dict_1.values():
    newlist.extend(val)
for j in newlist:
    counter += 1
print(counter)
