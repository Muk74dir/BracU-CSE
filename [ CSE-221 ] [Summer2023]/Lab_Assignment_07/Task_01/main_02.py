inpath = "C:\For-Github\BracU - CSE\[ CSE-221 ] [Summer2023]\Lab_Assignment_07\Task_01\input_01.txt"
infile = open(inpath, 'r')
outpath = "C:\For-Github\BracU - CSE\[ CSE-221 ] [Summer2023]\Lab_Assignment_07\Task_01\input_02.txt"
outfile = open(outpath, 'w')

n = int(infile.readline().strip())
print(n)
arr = []

for i in range(n):
    a, b = list(map(int, infile.readline().strip().split()))
    arr.append((a, b))

function = lambda x: x[1] 
sorted_tasks = sorted(arr, key=function)
print(sorted_tasks)

ans = []
ans.append(sorted_tasks[0])
for i in range(1, len(sorted_tasks)):
    if ans[-1][1] <= sorted_tasks[i][0]:
        ans.append(sorted_tasks[i])
    

print(ans)