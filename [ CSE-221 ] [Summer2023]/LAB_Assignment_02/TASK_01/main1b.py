inpath = "input1b.txt"
infile = open(inpath, 'r')

outpath = "output1b.txt"
outfile = open(outpath, 'w')

n, t = list(map(int, (infile.readline().strip().split())))
data = list(map(int, (infile.readline().strip().split())))

dict = {}

for i in range(n):
    rem = (t - data[i])
    if rem in dict:
        outfile.write(f"{dict[rem]} {i+1}")
        break
    else:
        dict[data[i]] = i+1
else:
    outfile.write("IMPOSSIBLE")

infile.close()
outfile.close()









