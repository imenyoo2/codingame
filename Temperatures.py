import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
list = []
absList = []
n = int(input())  # the number of temperatures to analyse
if n == 0:
    print('0')
else:
    for i in input().split():
        # t: a temperature expressed as an integer ranging from -273 to 5526
        t = int(i)
        list.append(t)
        absList.append(abs(t))
# Write an answer using print
    print(list, file=sys.stderr, flush=True)
    closeT = min(absList)
    if closeT * (-1) in list and closeT in list:
        print(str(closeT))
    elif closeT * (-1) in list and closeT not in list:
        print(str(closeT * (-1)))
    else:
        print(str(closeT))
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
