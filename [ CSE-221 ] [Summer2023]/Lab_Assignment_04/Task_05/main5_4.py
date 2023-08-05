inpath = "input5_4.txt"
infile = open(inpath, 'r')

outpath = "output5_4.txt"
outfile = open(outpath, 'w')

v, e, dest = list(map(int, infile.readline().strip().split()))
visited = [0 for i in range(v+1)]
level = [0 for y in range(v+1)]
parent = [0 for z in range(v+1)]

adj_list = [[]for i in range(v+1)]

for i in range(e):
    f, t = list(map(int, infile.readline().strip().split()))
    adj_list[f].append(t)
    adj_list[t].append(f)

def BFS_Traversal(adj_list, source):
    queue = []
    queue.append(source)
    visited[source] = 1
    level[source] = 0
    parent[source] = source

    while queue:
        temp = queue.pop(0)

        for x in adj_list[temp]:

            if visited[x] == 0:
                visited[x] = 1
                level[x] = level[temp] + 1
                parent[x] = temp
                queue.append(x)

            if x == dest:
                break

source = 1
BFS_Traversal(adj_list, source)


print(f"Time : {level[dest]}", file=outfile)


answer = []
while True:
    answer.append(dest)
    if dest == source:
        break
    dest = parent[dest]


answer.reverse()
print("Shortest Path: ", end="", file=outfile)
for x in answer:
    print(x, end = " ", file=outfile)


infile.close()
outfile.close()


