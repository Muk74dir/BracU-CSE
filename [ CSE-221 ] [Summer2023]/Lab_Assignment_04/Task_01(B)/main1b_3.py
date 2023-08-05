inpath = "input1b_3.txt"
infile = open(inpath, 'r')

outpath = "output1b_3.txt"
outfile = open(outpath, 'w')

v, e = list(map(int, infile.readline().strip().split()))

adj_list = [[] for i in range(v+1)]

for i in range(e):
    f, t, w = list(map(int, infile.readline().strip().split()))
    adj_list[f].append((t, w))


for i in range(v+1):
    print(i, ":", end= " ", file=outfile)
    for j in range(len(adj_list[i])):
        print(adj_list[i][j], end=" ", file=outfile)
    print(file=outfile)

infile.close()
outfile.close()