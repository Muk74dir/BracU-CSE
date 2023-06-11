inpath = "Task_03\input3.txt"
infile = open(inpath, 'r')

outpath = "Task_03\output3.txt"
outfile = open(outpath, 'w')

n = int(infile.readline().strip())
id = list(map(int, infile.readline().strip().split()))
mark = list(map(int, infile.readline().strip().split()))

data = {}


for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if mark[min_idx] < mark[j]:
            min_idx = j

        if mark[min_idx] == mark[j]:
            if id[min_idx] > id[j]:
                min_idx = j

    mark[i], mark[min_idx] = mark[min_idx], mark[i]
    id[i], id[min_idx] = id[min_idx], id[i]

for i in range(n):
    data[id[i]] = mark[i]
    outfile.write(f'ID: {id[i]} Mark: {mark[i]}\n')
    
infile.close()
outfile.close()