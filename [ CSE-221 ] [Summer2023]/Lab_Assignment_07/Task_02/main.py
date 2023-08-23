inpath = "input_04.txt"
infile = open(inpath, "r")
outpath = "output_04.txt"
outfile = open(outpath, "w")
tasks = []
task, people = list(map(int, infile.readline().split()))

def sorted_by_time(array): 
    ans = []
    ans.append(array[0])
    for i in range(1, len(array)):
        if ans[-1][1] <= array[i][0]:
            ans.append(array[i])
    return ans

for i in range(task):
    start, end = tuple(map(int, infile.readline().split()))
    tasks.append((start, end))

tasks.sort(key = lambda x: x[0])
assigned_tasks = []

for i in range(people):
    temp = sorted_by_time(tasks)
    assigned_tasks += temp
    tasks = [x for x in tasks if x not in temp]

outfile.write(str(len(assigned_tasks)) + "\n")
infile.close()
outfile.close()