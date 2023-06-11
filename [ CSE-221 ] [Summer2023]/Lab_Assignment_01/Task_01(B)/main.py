inpath = "Task_01(B)\input1b.txt"
file = open(inpath, 'r')

outpath = "Task_01(B)\output1b.txt" 
file2 = open(outpath, 'w')

n = file.readline().strip()

for i in range(int(n)):
    temp = file.readline().strip().split()
    if '+' in temp:
        file2.write(f'The result of {int(temp[1])} + {int(temp[3])} is {int(temp[1])+int(temp[3])}\n')
    elif '-' in temp : 
        file2.write(f'The result of {int(temp[1])} - {int(temp[3])} is {int(temp[1])-int(temp[3])}\n')
    elif '*' in temp :
        file2.write(f'The result of {int(temp[1])} * {int(temp[3])} is {int(temp[1])*int(temp[3])}\n')
    else:
        file2.write(f'The result of {int(temp[1])} / {int(temp[3])} is {int(temp[1])/int(temp[3])}\n')

file.close()
file2.close()