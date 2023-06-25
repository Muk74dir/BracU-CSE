inpath = "input3a.txt"
infile = open(inpath, 'r')
outpath = "output3a.txt"
outfile = open(outpath, 'w')

n = int(infile.readline().strip())
data = list(map(int, (infile.readline().strip().split())))



def merge_sort(data):
    if len(data) <= 1:
        return data
    
    mid = len(data) // 2
    sorted_left = merge_sort(data[:mid])
    sorted_right = merge_sort(data[mid:])
    sorted_data = []

    i, j = 0, 0
    while i < len(sorted_left) and j < len(sorted_right):
        if sorted_left[i] < sorted_right[j]:
            sorted_data.append(sorted_left[i])
            i += 1
        elif sorted_left[i] > sorted_right[j]:
            sorted_data.append(sorted_right[j])
            j += 1

        else:
            sorted_data.append(sorted_left[i])
            sorted_data.append(sorted_right[j])
            i += 1
            j += 1

    if i != len(sorted_left):
        sorted_data.extend(sorted_left[i:])
    else:
        sorted_data.extend(sorted_right[j:])
    
    return sorted_data


answer = merge_sort(data)

for i in answer:
    outfile.write(f"{i} ")

infile.close()
outfile.close()

    