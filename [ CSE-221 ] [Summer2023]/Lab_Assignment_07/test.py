import heapq

inpath = "C:\\For-Github\\BracU - CSE\\[ CSE-221 ] [Summer2023]\\Lab_Assignment_07\\Task_02\\input.txt"
infile = open(inpath, "r")
outpath = "C:\\For-Github\\BracU - CSE\\[ CSE-221 ] [Summer2023]\\Lab_Assignment_07\\Task_02\\output.txt"
outfile = open(outpath, "w")

tasks = []
task, people = list(map(int, infile.readline().split()))

for i in range(task):
    start, end = tuple(map(int, infile.readline().split()))
    tasks.append((start, end))

def max_tasks(tasks, people):
    # Sort tasks by end times
    tasks.sort(key=lambda x: x[1])

    # Create a min heap of people's availability based on start times
    available_people = [0] * people
    heapq.heapify(available_people)

    tasks_assigned = 0
    for start, end in tasks:
        if available_people and available_people[0] <= start:
            heapq.heappop(available_people)  # Remove the earliest available person
            heapq.heappush(available_people, end)  # Update their availability
            tasks_assigned += 1

    return tasks_assigned

result = max_tasks(tasks, people)
print(result)
outfile.write(str(result) + "\n")

infile.close()
outfile.close()
