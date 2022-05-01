sample = input()
temp = sample[1:-1].split(", ")
fresh = list()
counter = int()
result = int()
for i in temp:
    fresh.append(i.split(": "))
for i in fresh:
    for j in i:
        if j.isdigit():
            result += int(j)
            counter += 1
print("Average is", int(result / counter), end=".")
