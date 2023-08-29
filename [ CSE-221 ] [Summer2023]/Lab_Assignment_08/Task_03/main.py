import math

inpath = "C:\For-Github\BracU - CSE\[ CSE-221 ] [Summer2023]\Lab_Assignment_08\Task_03\input_01.txt"
infile = open(inpath, 'r')
outpaht = "C:\For-Github\BracU - CSE\[ CSE-221 ] [Summer2023]\Lab_Assignment_08\Task_03\output_01.txt"
outfile = open(outpaht, 'w')

type, target = map(int, infile.readline().strip().split())
coins = list(map(int, infile.readline().strip().split()))

def Min_Coin_Change(type, target, coins):
    if target == 0:
        return 0
    if target < 0:
        return math.inf
    if type <= 0 and target >= 1:
        return math.inf
    return min(Min_Coin_Change(type-1, target, coins), 1 + Min_Coin_Change(type, target-coins[type-1], coins))

if Min_Coin_Change(type, target, coins) == math.inf:
    outfile.write("-1")
else:
    outfile.write(str(Min_Coin_Change(type, target, coins)))

infile.close()
outfile.close()