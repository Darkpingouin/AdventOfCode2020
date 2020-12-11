import sys
import copy

nbseated = 0

def change_state(boat, boat2, x, y):
    nbtaken = 0
    nbempty = 0
    maxX = len(boat)
    maxY = len(boat[0])
    if (x - 1 >= 0):
        if (boat[x-1][y] == 'L'):
            nbempty += 1
        elif(boat[x-1][y] == '#'):
            nbtaken += 1
    if (x + 1 < maxX):
        if (boat[x+1][y] == 'L'):
            nbempty += 1
        elif(boat[x+1][y] == '#'):
            nbtaken += 1
    if (y - 1 >= 0):
        if (boat[x][y-1] == 'L'):
            nbempty += 1
        elif(boat[x][y-1] == '#'):
            nbtaken += 1
    if (y + 1 < maxY):
        if (boat[x][y+1] == 'L'):
            nbempty += 1
        elif(boat[x][y+1] == '#'):
            nbtaken += 1
    if (y + 1 < maxY and x - 1 >= 0):
        if (boat[x-1][y+1] == 'L'):
            nbempty += 1
        elif(boat[x-1][y+1] == '#'):
            nbtaken += 1
    if (y + 1 < maxY and x + 1 < maxX):
        if (boat[x+1][y+1] == 'L'):
            nbempty += 1
        elif(boat[x+1][y+1] == '#'):
            nbtaken += 1
    if (y - 1 >= 0 and x + 1 < maxX):
        if (boat[x+1][y-1] == 'L'):
            nbempty += 1
        elif(boat[x+1][y-1] == '#'):
            nbtaken += 1
    if (y - 1 >= 0 and x - 1 >= 0):
        if (boat[x-1][y-1] == 'L'):
            nbempty += 1
        elif(boat[x-1][y-1] == '#'):
            nbtaken += 1
    seat = boat[x][y]      
    if (nbtaken == 0 and seat == 'L'):
        boat2[x][y] = '#'
        return 1
    if (nbtaken >= 4 and seat == '#'):
        boat2[x][y] = 'L'
        return 1
    return 0
    
def seat_people(boat, nbseated):
    boat2 = copy.deepcopy(boat)
    nbseated[0] = 0
    for x in range(0, len(boat)):
        nbseatedY = 0
        for y in range(0, len(boat[0])):
            if (boat[x][y] != '.'):
                nbseatedY += change_state(boat, boat2, x, y)
        nbseated[0] += nbseatedY
    return(boat2)

        

def main():
    imput = sys.stdin.read().split("\n")
    boat = []
    nbseated = [1]
    for line in imput:
        boat.append(list(line))
    print(boat)
    nb = 0
    while(nbseated[0] > 0):
        boat = seat_people(boat, nbseated)
    print(boat)
    print(nbseated[0])
    total = 0
    for line in boat:
        for chair in line:
            if chair == "#":
                total += 1
    print(total)

main()
