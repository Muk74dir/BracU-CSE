inpath = "input2a.txt"
infile = open(inpath, 'r')

outpath = "output2a.txt"
outfile = open(outpath, 'w')

n1 = int(infile.readline().strip())
data1 = list(map(int, (infile.readline().strip().split())))
n2 = int(infile.readline().strip())
data2 = list(map(int, (infile.readline().strip().split())))

result = data1 + data2
result.sort()

for i in range(len(result)):
    outfile.write(f"{result[i]} ")

infile.close()
outfile.close()
