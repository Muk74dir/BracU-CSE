inpath = "inputA_3.txt"
infile = open(inpath, "r")

outpath = "outputA_3.txt"
outfile = open(outpath, "w")

v, e = list(map(int, infile.readline().strip().split()))
adj_list = [[] for i in range(v+1)]
visited = [0 for i in range(v+1)]
visited_cycle = [0 for i in range(v+1)]
stack = []

def DFS_Traversal(source):
    visited[source] = 1
    for adj_node in adj_list[source]:
        if visited[adj_node] == 0:
            DFS_Traversal(adj_node)
    stack.append(source)

def Cycle_Detect(selected):
    visited_cycle[selected] = 1
    for adj_node in adj_list[selected]:
        if visited_cycle[adj_node] == 0:
            Got_Cycle = Cycle_Detect(adj_node)
            if(Got_Cycle):
                return True
        elif visited_cycle[adj_node] == 1:
            return True

    visited_cycle[selected] = 2
    return False

for i in range(1, (e+1)):
    f, t = list(map(int, infile.readline().strip().split()))
    adj_list[f].append(t)
    

Cycle_Exist = False
for i in range(1, v+1):
    if visited_cycle[i] == 0:
        is_Cyclic= Cycle_Detect(i)
        if is_Cyclic:
            Cycle_Exist = True
            break
    
if Cycle_Exist:
    print("IMMPOSSIBLE", file=outfile)
else:  
    for i in range(1, (v+1)):
        if visited[i] == 0:
            DFS_Traversal(i)

    while len(stack) != 0:
        print(stack.pop(-1), end=" ", file=outfile)

infile.close()
outfile.close()