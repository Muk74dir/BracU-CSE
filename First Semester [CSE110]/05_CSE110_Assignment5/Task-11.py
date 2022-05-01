sample = str(input())[1:-1].lower()
new_dict = {}
for i in sample:
    if i == " ":
        continue
    else:
        count = int()
        for j in range(len(sample)):
            if i == sample[j]:
                count += 1
    new_dict[i] = count
print(new_dict)
