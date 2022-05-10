given_inp = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
newList = []
for i in given_inp:
    newList.append(i)
newList.reverse()
print(tuple(newList))