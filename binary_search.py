from glob import glob
import re
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
w -= 1
h -= 1
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
wmin, hmin = 0,0
# game loop

def getNewCoord(coord, lim, dir):
    if abs(coord - lim) == 1:
        if dir:
            return coord + 1
        else:
            return coord - 1
    elif dir:
        return math.floor(coord + abs((lim - coord)/2))
    else:
        return math.floor(coord - abs((lim - coord)/2))

def applyChanges(dir):
    global h, w, hmin, wmin, x0, y0
    if dir == 'L':
        w = x0
        x0 = getNewCoord(x0, wmin, 0)
    elif dir == 'R':
        wmin = x0
        x0 = getNewCoord(x0, w, 1)
    elif dir == 'U':
        h = y0
        y0 = getNewCoord(y0, hmin, 0)
    else:  #D
        hmin = y0
        y0 = getNewCoord(y0, h, 1)

while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    if len(bomb_dir) == 1:
        applyChanges(bomb_dir)
    else:
        applyChanges(bomb_dir[0])
        applyChanges(bomb_dir[1])

    print(bomb_dir, file=sys.stderr, flush=True)
    print(f"{str(x0)} {str(y0)}")
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # the location of the next window Batman should jump to.
    #print("0 0")
