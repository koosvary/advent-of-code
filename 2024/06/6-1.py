# get the map into a 2D array
# keep going up until you get to a hash
# leave X's behind at last spot
# rotate the map 90 degrees like it's a matrix
# thanks stack overflow:
#   [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]
# keep going till out of bounds
# count X's

map = [];
startX = -1;
startY = -1;

def printMap():
    for row in map:
        print(row)
    print('===============')

def findCaret():
    global startX, startY;
    for i, row in enumerate(map):
        for j, char in enumerate(row):
            if char == "^":
                startY, startX = i, j;

def countXs():
    total = 0;
    for i, row in enumerate(map):
        for j, char in enumerate(row):
            if char == "X":
                total += 1;
    return total

def rotateMapCounterClockwise():
    global map;
    map = [[map[j][i] for j in range(len(map))] for i in range(len(map[0])-1,-1,-1)]

def goUpUntilStopped(x, y):
    global map;

    if y == 0: 
        # Found a way out of the map
        map[y][x] = 'X';
        return True;

    newY = y-1;
    if map[newY][x] == '#':
        map[y][x] = '^'
        return False; # Can't go anymore up, but not OoB

    map[y][x] = 'X'
    return goUpUntilStopped(x, newY); # Not done yet

def traverseMap():
    while True:
        findCaret();
        done = goUpUntilStopped(startX, startY);
        if done:
            break;
        rotateMapCounterClockwise();

with open('2024/06/testinput.txt') as f:
    for line in f:
        row = [];
        for c in line.strip():
            row.append(c);
        map.append(row);
    
    traverseMap();
    for row in map:
        print(row)
    print(countXs());

