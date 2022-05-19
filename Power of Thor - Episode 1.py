import sys
import math

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
# the vectors in wich thor moves in every direction
rightDirs = [
        [0, -1],
        [1, -1],
        [1, 0],
        [1, 1],
        [0, 1],
    ]
leftDirs = [
        [-1, -1],
        [-1, 0],
        [-1, 1],
]

# movement commands
# i saperated the right movs and the left ones to seperate the movs with the same 
# angle, for example SE => pi/4 and SW => pi/4
rightMovs = ["N", "NE", "E", "SE", "S"]
leftMovs = ["NW", "W", "SW"]

# the angles of every direction (for example N => pi)
# the angles are taken with respect to the y direction or [0, 1] vector
rightAngles = [1*math.pi, 3/4*math.pi, 1/2*math.pi, 1/4*math.pi, 0]
leftAngles = [3/4*math.pi, 1/2*math.pi, 1/4*math.pi]

def move(angle, angList, movsList, dirsList):
    global initial_tx, initial_ty
    i = 0
    for ang in angList:
        # the thor->light angle might not be exaclly equal to the movs angles
        # so we have this interval
        if ang - math.pi*1/8 <= angle <= ang + math.pi*1/8:
            print(movsList[i])
            # changing to the new position 
            initial_tx += dirsList[i][0]
            initial_ty += dirsList[i][1]
            break
        i += 1

def ComputeAngle(x, y):
    # calculate the angle between [0, 1] and [x, y]
    angle = math.acos((0 + 1 * y)/(math.sqrt(1) * math.sqrt(x*x + y*y)))
    # checking wich movmens thor has to do, right movs or left movs
    if initial_tx <= light_x:
        move(angle, rightAngles, rightMovs, rightDirs)
    else:
        move(angle, leftAngles, leftMovs, leftDirs)


while True:
    remaining_turns = int(input())
    # computing the vector from thor to the light
    vect = [light_x - initial_tx, light_y - initial_ty]

    ComputeAngle(vect[0], vect[1])



