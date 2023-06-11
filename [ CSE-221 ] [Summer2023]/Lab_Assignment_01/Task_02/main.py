inpath = "Task_02\input2.txt"
infile = open(inpath, 'r')

outpath = "Task_02\output2.txt"
outfile = open(outpath, 'w')

n = int(infile.readline().strip())

data = list(map(int, infile.readline().strip().split()))

def bubbleSort(arr):
    for i in range(len(arr)-1):
        swap = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if(swap == False):
            break

    return arr

for i in (bubbleSort(data)):
    outfile.write(f'{i} ')

# Comment : 
"""

To achieve a best-case time complexity of θ(n) for the Bubble Sort algorithm, 
the array should already be sorted. In the best-case scenario, 
the array is in ascending order, and no swaps are required during the sorting process.

"""

infile.close()
outfile.close()