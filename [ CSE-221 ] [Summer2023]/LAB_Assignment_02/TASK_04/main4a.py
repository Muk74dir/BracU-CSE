import math

inpath = "input4a.txt"
infile = open(inpath, 'r')
outpath = "output4a.txt"
outfile = open(outpath, 'w')

n = int(infile.readline().strip())
data = list(map(int, (infile.readline().strip().split())))

def div_and_conq(data, maxvalue = -math.inf):
    if len(data) == 1:
        return data, data[0]
    
    elif len(data) == 2:
        if data[0] > data[1]:
            maxvalue = data[0]
        else:
            maxvalue = data[1]
        return data, maxvalue 

    mid = len(data) // 2
    left = div_and_conq(data[:mid], maxvalue)
    right = div_and_conq(data[mid:], maxvalue)

    if left[1] > right[1]:
        maxvalue = left[1]
    else:
        maxvalue = right[1]

    return left[0] + right[0], maxvalue

outfile.write(str(div_and_conq(data)[1]))


infile.close()
outfile.close()