import math 
import heapq

inpath = "input_01.txt"
outpath = "output_01.txt"

infile = open(inpath, 'r')
outfile = open(outpath, 'w')

v, e = map(int, infile.readline().strip().split())
adj_list = [[] for i in range(v + 1)]
dist = [math.inf for k in range(v + 1)]

def Dijkstra(source, dest):
    dist[source] = 0
    pq = []
    heapq.heappush(pq, (0, source))
    
    while pq:
        danger, cur_node = heapq.heappop(pq)
        for adj_node, edge_cost in adj_list[cur_node]:
            new_danger = max(danger, edge_cost)
            if new_danger < dist[adj_node]:
                dist[adj_node] = new_danger
                heapq.heappush(pq, (new_danger, adj_node))

for i in range(e):
    f, t, w = map(int, infile.readline().strip().split())
    adj_list[f].append((t, w))

src = 1
dest = v
Dijkstra(src, dest)

min_danger_level = dist[dest]
if min_danger_level == math.inf:
    outfile.write("Impossible")
else:
    outfile.write(str(min_danger_level))

infile.close()
outfile.close()
