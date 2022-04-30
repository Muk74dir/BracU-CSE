list_1 = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]
new_dict = {}
newList = []
for j in range(len(list_1)):
    if list_1[j][0] not in new_dict.keys():
        new_dict[list_1[j][0]] = newList
print(new_dict)
