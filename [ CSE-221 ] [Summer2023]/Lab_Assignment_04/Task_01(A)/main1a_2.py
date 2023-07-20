inpath = "input1a_2.txt"
infile = open(inpath, 'r')

outpath = "output1a_2.txt"
outfile = open(outpath, 'w')

v, e = list(map(int, infile.readline().strip().split()))

adj_matrix = [[0 for i in range(v+1)] for j in range(v+1)]

for i in range(e):
    f, t, w =  list(map(int, infile.readline().strip().split()))
    adj_matrix[f][t] = w


for i in range(v+1):
    for j in range(v+1):
        outfile.write(str(adj_matrix[i][j]) + " ")
    outfile.write("\n")
