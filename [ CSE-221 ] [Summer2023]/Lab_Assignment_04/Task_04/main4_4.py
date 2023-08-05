inpath = "input4_4.txt"
infile = open(inpath, 'r')

outpath = "output4_4.txt"
outfile = open(outpath, 'w')

v, e = list(map(int, infile.readline().strip().split()))
visited = [0 for i in range(v+1)]

adj_list = [[]for i in range(v+1)]

for i in range(e):
    f, t = list(map(int, infile.readline().strip().split()))
    adj_list[f].append(t)


def Cycle_Detect(adj_list, selected):
    visited[selected] = 1
    
    for adj_node in adj_list[selected]:
        if visited[adj_node] == 0:
            Got_Cycle = Cycle_Detect(adj_list, adj_node)
            if(Got_Cycle):
                return True
            
        elif visited[adj_node] == 1:
            return True

    visited[selected] = 2
    return False

Cycle_Exist = False

for i in range(1, v+1):
    if visited[i] == 0:
        is_Cyclic= Cycle_Detect(adj_list, i)
        if is_Cyclic:
            Cycle_Exist = True
            break
    
if Cycle_Exist:
    print("YES", file=outfile)
else:
    print("NO", file=outfile)


infile.close()
outfile.close()
