inpath = "input_02.txt"
infile = open(inpath, 'r')
outpath = "output_02.txt"
outfile = open(outpath, 'w')

city, road = map(int, infile.readline().split())
adj_list = [ [] for i in range(city + 1) ]
visited = [ 0 for i in range(city + 1) ]

for i in range(road):
    f, t, w = map(int, infile.readline().split())
    adj_list[f].append((t, w))
    adj_list[t].append((f, w))

def MinimumCost(adj_list, visited):
    pq = []
    cost = 0
    visited[1] = 1
    for i in adj_list[1]:
        pq.append(i)
    while pq:
        pq.sort(key = lambda x: x[1])
        u, w = pq.pop(0)
        if visited[u] == 0:
            visited[u] = 1
            cost += w
            for i in adj_list[u]:
                pq.append(i)
    return cost

print(MinimumCost(adj_list, visited) , file = outfile)

infile.close()
outfile.close()