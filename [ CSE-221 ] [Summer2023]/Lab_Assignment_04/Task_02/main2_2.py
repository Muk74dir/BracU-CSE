inpath = "input2_2.txt"
infile = open(inpath, 'r')

outpath = "output2_2.txt"
outfile = open(outpath, 'w')

v, e = list(map(int, infile.readline().strip().split()))
visited = [0 for i in range(v+1)]

adj_list = [[]for i in range(v+1)]

for i in range(e):
    f, t = list(map(int, infile.readline().strip().split()))
    adj_list[f].append(t)
    adj_list[t].append(f)

def BFS_Traversal(adj_list, source):
    queue = []
    queue.append(source)
    visited[source] = 1

    while queue:
        temp = queue.pop(0)
        print(temp, end=" ", file=outfile)

        for x in adj_list[temp]:
            if visited[x] == 0:
                visited[x] = 1
                queue.append(x)

source = 1
BFS_Traversal(adj_list, source)

infile.close()
outfile.close()







