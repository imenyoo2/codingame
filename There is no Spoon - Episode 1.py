import sys
import math

x, y = [0, 0]
coords = []
width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
for i in range(height):
    x = 0
    l = []
    line = input()  # width characters, each either 0 or .
    #print(line, file=sys.stderr, flush=True)
    for i in line:
        if i == '0':
            l.append(f'{str(x)} {str(y)}')
            x += 1
        else:
            l.append('-1 -1')
            x += 1
    y += 1
    coords.append(l)

i = 0
while i < len(coords):
    j = 0
    while j < len(coords[i]):
        c = coords[i][j]
        if c == '-1 -1':
            j += 1
            continue
        try:
            while 1:
                r = coords[i][j+1]
                if r != '-1 -1':
                    break
                j += 1
        except:
            r = '-1 -1'
        try:
            while 1:
                l = coords[i+1][j]
                if l != '-1 -1':
                    break
                i += 1
        except:
            l = '-1 -1'
        print(c, r, l, file=sys.stdout, flush=True)
        j += 1

    i += 1
