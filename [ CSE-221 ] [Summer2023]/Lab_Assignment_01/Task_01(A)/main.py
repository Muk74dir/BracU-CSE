inpath = "Task_01(A)\input1a.txt"
file = open(inpath, 'r')

outpath = "Task_01(A)\output1a.txt"
file2 = open(outpath, 'w')

n = file.readline().strip()

for i in range(int(n)):
    temp = file.readline().strip()
    if int(temp) % 2 == 0:
        file2.write(f'{temp} is an Even number\n')
    else:
        file2.write(f'{temp} is an Odd number\n')

file.close()
file2.close()