import heapq

inpath = "C:\For-Github\BracU - CSE\[ CSE-221 ] [Summer2023]\Lab_Assignment_07\Task_02\input_04.txt"
infile = open(inpath, "r")
outpath = "C:\For-Github\BracU - CSE\[ CSE-221 ] [Summer2023]\Lab_Assignment_07\Task_02\output_04.txt"
outfile = open(outpath, "w")
tasks = []
task, people = list(map(int, infile.readline().split()))

for i in range(task):
    start, end = tuple(map(int, infile.readline().split()))
    tasks.append((start, end))

def sorted_tasks(array):
    ans = []
    ans.append(array[0])
    ini_sorted_tasks = sorted(array, key=lambda x: x[1])
    for i in range(1, len(ini_sorted_tasks)):
        if ans[-1][1] <= ini_sorted_tasks[i][0]:
            ans.append(ini_sorted_tasks[i])
    return ans


diff_sorted_tasks = sorted(tasks, key=lambda x: abs(x[0] - x[1]), reverse=True)

cnt = 0
for i in range(people):
    diff = abs(diff_sorted_tasks[i][0] - diff_sorted_tasks[i][1])

    sorted_by_start_end = sorted_tasks(diff_sorted_tasks)
    i = 0
    while i < len(diff_sorted_tasks):
        if diff == abs(diff_sorted_tasks[i][0] - diff_sorted_tasks[i][1]):
            diff_sorted_tasks.remove(diff_sorted_tasks[i])
            cnt += 1
        i += 1
    
outfile.write(str(cnt+1))

infile.close()
outfile.close()