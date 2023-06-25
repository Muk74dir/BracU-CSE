inpath = "input2b.txt"
infile = open(inpath, 'r')

outpath = "output2b.txt"
outfile = open(outpath, 'w')

n1 = int(infile.readline().strip())
data1 = list(map(int, (infile.readline().strip().split())))
n2 = int(infile.readline().strip())
data2 = list(map(int, (infile.readline().strip().split())))

result = []

i = 0
j = 0

while i<n1 and j<n2:
    if data1[i] < data2[j]:
        result.append(data1[i])
        i += 1
    elif data1[i] > data2[j]:
        result.append(data2[j])
        j += 1
    elif data1[i] == data2[j]:
        result.append(data1[i])
        result.append(data2[j])
        i += 1
        j += 1

if i != n1:
    result += data1[i:]
if j != n2:
    result += data2[j:]

for i in range(len(result)):
    outfile.write(f"{result[i]} ")

infile.close()
outfile.close()