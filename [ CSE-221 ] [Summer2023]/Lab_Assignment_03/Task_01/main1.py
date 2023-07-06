inpath = "input1.txt"
infile = open(inpath, 'r')

outpath = "output1.txt"
outfile = open(outpath, 'w')

n = int(infile.readline().strip())
data = list(map(int, (infile.readline().strip().split())))

def divide_n_conqure(data, cnt=0):
    if len(data) <= 1:
        return data, cnt
    
    mid_ind = len(data)//2
    left = data[:mid_ind]
    right = data[mid_ind:]


    sorted_left, cnt_left = divide_n_conqure(left, cnt)
    sorted_right, cnt_right = divide_n_conqure(right, cnt)

    sorted_all = []

    i, j = 0, 0

    while i < len(sorted_left) and j < len(sorted_right):
        if sorted_left[i] < sorted_right[j]:
            sorted_all.append(sorted_left[i])
            i += 1

        elif sorted_left[i] > sorted_right[j]:
            sorted_all.append(sorted_right[j])

            cnt += len(sorted_left) - i
            j += 1

        elif sorted_left[i] == sorted_right[j]:
            sorted_all.append(sorted_left[i])
            sorted_all.append(sorted_right[j])
            i += 1
            j += 1

    sorted_all.extend(sorted_left[i:])
    sorted_all.extend(sorted_right[j:])

    return sorted_all, cnt_left+cnt+cnt_right

outfile.write(str(divide_n_conqure(data)[1]))

infile.close()
outfile.close()
