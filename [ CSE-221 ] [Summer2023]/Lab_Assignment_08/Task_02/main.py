inpath = "input_04.txt"
infile = open(inpath, 'r')
outpath = "output_04.txt"
outfile = open(outpath, 'w')

fredy = int(infile.readline().strip())
arr = [ 0 for x in range(fredy+1)]

def Jump_Count(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    
    if arr[n] == 0:
        arr[n] = Jump_Count(n-1) + Jump_Count(n-2)
    return arr[n]

outfile.write(str(Jump_Count(fredy)))

infile.close()
outfile.close()