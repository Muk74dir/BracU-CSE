inpath = "C:\For-Github\BracU - CSE\[ CSE-221 ] [Summer2023]\Lab_Assignment_07\Task_02\input.txt"
infile = open(inpath, "r")
outpath = "C:\For-Github\BracU - CSE\[ CSE-221 ] [Summer2023]\Lab_Assignment_07\Task_02\output.txt"
outfile = open(outpath, "w")
tasks = []
task, people = list(map(int, infile.readline().split()))

for i in range(task):
    start, end = tuple(map(int, infile.readline().split()))
    tasks.append((start, end))

def sorted_tasks_by_diff(array):
    ans = []
    ini_sorted_tasks = sorted(array, key=lambda x: x[1])
    ans.append(ini_sorted_tasks[0])
    for i in range(1, len(ini_sorted_tasks)):
        if ans[-1][1] <= ini_sorted_tasks[i][0]:
            ans.append(ini_sorted_tasks[i])
    return ans


diff_sorted_tasks = sorted(tasks, key=lambda x: abs(x[0] - x[1]), reverse=True)
print(diff_sorted_tasks)
cnt = 0

for i in range(people):
    diff = abs(diff_sorted_tasks[i][0] - diff_sorted_tasks[i][1])
    
    print(diff) # 4
    sorted_tasks = sorted_tasks_by_diff(diff_sorted_tasks)
    j = 0 
    while j < len(sorted_tasks):
        if abs(sorted_tasks[j][0] - sorted_tasks[j][1]) == diff:
            diff_sorted_tasks.pop(0)
            cnt += 1
            print(sorted_tasks[j])
        j += 1
    
    print(diff_sorted_tasks)