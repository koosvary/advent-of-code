import stopit # get some help

originalMap = [];
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

@stopit.threading_timeoutable(default=False)
def traverseMap():
    while True:
        findCaret();
        done = goUpUntilStopped(startX, startY);
        if done:
            break;
        rotateMapCounterClockwise();
    return True;

# This one's real shit. If you're running it, clear your day. 
with open('2024/06/input.txt') as f:
    for i, line in enumerate(f):
        row = [];
        for c in line.strip():
            row.append(c);
        originalMap.append(row);
    
    
    loops = 0;
    for i, row in enumerate(originalMap):
        for j, char in enumerate(row):
            map = [row[:] for row in originalMap];
            print(map)
            if map[i][j] != '.':
                continue;
    
            map[i][j] = '#';
            if not traverseMap(timeout=1):
                print(f'{i}, {j} was good')
                loops += 1;
            else:
                print(f'{i}, {j} sucked')


    print(loops);
