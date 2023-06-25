inpath = "input1a.txt"
infile = open(inpath, 'r')

outpath = "output1a.txt"
outfile = open(outpath, 'w')

n, t = list(map(int, (infile.readline().strip().split())))
data = list(map(int, (infile.readline().strip().split())))

flag = False
for i in range(n):
    for j in range(i+1, n):
        if data[i] + data[j] == t:
            outfile.write(f"{i+1} {j+1}")
            flag = True
    break

if flag != True:
    outfile.write("IMPOSSIBLE")

infile.close()
outfile.close()