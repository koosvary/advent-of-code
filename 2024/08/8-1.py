
antiNodes = {};
antenna = {}
map = [];
width = -1;
height = -1;

def inBounds(x, y):
    if x < 0 or x >= width:
        return False
    if y < 0 or y >= height:
        return False
    return True

def makeNode(fromX, fromY, xDir, yDir):
    newX = fromX + xDir;
    newY = fromY + yDir;
    if inBounds(newX, newY):
        antiNodes[newX+1, newY+1] = True;

with open('2024/08/input.txt') as f:
    total = 0;
    for x, line in enumerate(f):
        line = line.strip()
        map.append(line)
        for y, char in enumerate(line):
            if char != '.':
                if char not in antenna.keys():
                    antenna[char] = []
                antenna[char].append(f'{x},{y}');
    
    height = len(map)
    width = len(map[0])
    
    
    for key in antenna.keys():
        spots = antenna[key];
        for i, first in enumerate(spots):
            firstX = int(first.split(',')[0])
            firstY = int(first.split(',')[1])
            for j in range(i+1, len(spots)):
                second = spots[j]
                secondX = int(second.split(',')[0])
                secondY = int(second.split(',')[1])

                xDiff = firstX - secondX;
                yDiff = firstY - secondY;

                # first antinode
                makeNode(firstX, firstY, xDiff, yDiff)
                
                # second antinode
                makeNode(secondX, secondY, -xDiff, -yDiff)

print(len(antiNodes))