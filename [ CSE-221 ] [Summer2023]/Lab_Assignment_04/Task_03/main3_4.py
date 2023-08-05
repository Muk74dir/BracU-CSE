inpath = "input3_4.txt"
infile = open(inpath, 'r')

outpath = "output3_4.txt"
outfile = open(outpath, 'w')

v, e = list(map(int, infile.readline().strip().split()))
visited = [0 for i in range(v+1)]
adj_list = [[]for i in range(v+1)]

for i in range(e):
    f, t = list(map(int, infile.readline().strip().split()))
    adj_list[f].append(t)
    adj_list[t].append(f)


def DFS_Traversal(adj_list, selected):
    visited[selected] = 1
    print(selected, end=" ", file=outfile)
    for adj_node in adj_list[selected]:
        if visited[adj_node] == 0:
            DFS_Traversal(adj_list, adj_node)

selected = 1

DFS_Traversal(adj_list, selected)


infile.close()
outfile.close()