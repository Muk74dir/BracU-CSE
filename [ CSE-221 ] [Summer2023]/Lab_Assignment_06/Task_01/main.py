import math 

inpath = "input_02.txt"
infile = open(inpath, 'r')
outpath = "output_02.txt"
outfile = open(outpath, 'w')

v, e = list(map(int, infile.readline().strip().split()))
adj_list= [[] for i in range(v+1)]
visited = [0 for j in range(v+1)]
dist = [math.inf for k in range(v+1)]



def Dijkstra(source):

    dist[source] = 0
    for i in range(1, v):
        selected = -1
        for j in range(1, v):
            if visited[j] == 0 and (dist[j] < dist[selected] or selected == -1):
                selected = j

        visited[selected] = 1
        
        for adj_pair in adj_list[selected]:
            if dist[adj_pair[0]] > dist[selected] + adj_pair[1]:
                dist[adj_pair[0]] = dist[selected] + adj_pair[1]

for i in range(e):
    f, t, w = list(map(int, infile.readline().strip().split()))
    adj_list[f].append((t, w))


src = int(infile.readline().strip())

Dijkstra(src)
for i in range(1, v+1):
    if dist[i] == math.inf:
        outfile.write("-1 ")
    else:
        outfile.write(str(dist[i]) + " ")


infile.close()
outfile.close()