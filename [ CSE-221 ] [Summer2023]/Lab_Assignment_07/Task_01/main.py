inpath = "input_03.txt"
infile = open(inpath, 'r')
outpath = "output_03.txt"
outfile = open(outpath, 'w')

n = int(infile.readline().strip())
arr = []

for i in range(n):
    a, b = list(map(int, infile.readline().strip().split()))
    arr.append((a, b))

function = lambda x: x[1] 
sorted_tasks = sorted(arr, key=function)

ans = []
ans.append(sorted_tasks[0])
for i in range(1, len(sorted_tasks)):
    if ans[-1][1] <= sorted_tasks[i][0]:
        ans.append(sorted_tasks[i])

outfile.write(f"{len(ans)}\n")
for i in ans:
    outfile.write(f"{i[0]} {i[1]}\n")