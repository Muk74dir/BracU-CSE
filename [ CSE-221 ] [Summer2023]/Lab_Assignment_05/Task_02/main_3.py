import heapq

inpath = "input_2.txt"
infile = open(inpath, "r")

outpath = "output_2.txt"
outfile = open(outpath, "w")

v, e = list(map(int, infile.readline().strip().split()))
adj_list = [[] for i in range(v+1)]
visited = [0 for i in range(v+1)]
visited_cycle = [0 for i in range(v+1)]
indegre = [0 for i in range(v+1)]


def BFS_Topological_Sort(adj_list, indegree):
    queue = []
    for i in range(1, (v+1)):
        if indegree[i] == 0:
            heapq.heappush(queue, i)
    result = []      
    while queue:
        temp = heapq.heappop(queue)
        result.append(temp)
        for adj_node in adj_list[temp]:
            indegree[adj_node] -= 1
            if indegree[adj_node] == 0:
                heapq.heappush(queue, adj_node)
    return result
                
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
    indegre[t] += 1
    

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
    print(*BFS_Topological_Sort(adj_list, indegre), file=outfile)
  

infile.close()
outfile.close()