import math 
import heapq

inpath = "input_01.txt"
infile = open(inpath, 'r')
outpath = "output_01.txt"
outfile = open(outpath, 'w')

v, e = list(map(int, infile.readline().strip().split()))
adj_list= [[] for i in range(v+1)]
visited_alice = [0 for j in range(v+1)]
visited_bob = [0 for j in range(v+1)]
dist_alice = [math.inf for k in range(v+1)]
dist_bob = [math.inf for k in range(v+1)]


def Dijkstra(source, visited, dist):
    dist[source] = 0
    pq = []
    heapq.heappush(pq, (0, source))
    while pq:
        dst, node = heapq.heappop(pq)
        if visited[node] == 1:
            continue
        visited[node] = 1

        for adj_node, edge_cost in adj_list[node]:
            if dist[adj_node] > dist[node] + edge_cost:
                dist[adj_node] = dist[node] + edge_cost
                heapq.heappush(pq, (dist[adj_node], adj_node))

for i in range(e):
    f, t, w = list(map(int, infile.readline().strip().split()))
    adj_list[f].append((t, w))


alice, bob = list(map(int, infile.readline().strip().split()))

by_alice = Dijkstra(alice, visited_alice, dist_alice)
by_bob = Dijkstra(bob, visited_bob, dist_bob)

immposibility = True
distance = math.inf

for i in range(1, v+1):
    if visited_alice[i] == 1 and visited_bob[i] == 1:
        immposibility = False
        if distance > min(distance, max(dist_alice[i], dist_bob[i])): 
            distance = min(distance, max(dist_alice[i], dist_bob[i]))
            node = i

if immposibility == True:
    print("IMPOSSIBLE")
else:
    print(f"Time {distance}", file=outfile)
    print(f"Node {node}", file=outfile)

infile.close()
outfile.close()