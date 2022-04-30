sample = input().split(", ")
temp = sample[2:-2]
result = []
for i in temp:
    result.append(int(i))
print(tuple(result))
