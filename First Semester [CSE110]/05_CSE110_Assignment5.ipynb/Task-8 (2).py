sample = input()
temp = sample[1:-1].split(", ")
new_dict = {}
result = int()
counter = int()
for i in temp:
    single = i.split(": ")
    new_dict[single[0]] = single[1]
for j in new_dict.values():
    result += int(j)
    counter += 1
print("Average is", int(result / counter), end=".") 
