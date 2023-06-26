import math
inpath = "input2.txt"
infile = open(inpath, 'r')

outpath = "output2.txt"
outfile = open(outpath, 'w')

n = int(infile.readline().strip())
data = list(map(int, (infile.readline().strip().split())))

max_value = -math.inf

def mergesort(data, max_value):
    if len(data) <= 2:
        return data, max_value

    mid_ind = len(data)//2

    left = data[:mid_ind]
    right = data[mid_ind:]

    sorted_left, max_value = mergesort(left, max_value)
    sorted_right, max_value = mergesort(right, max_value)

    sorted_all = []

    







    sorted_all.extend(sorted_left[i:])
    sorted_all.extend(sorted_right[j:])

    return sorted_all, max_value