import functools

map = {}
moves = []
currentPosition = startPosition = (-1, -1)
width = height = 0
total = 0

def calcGpsCoords():
    global total
    for i in range(height):
        for j in range(width):
            if map[i,j] == '[':
                total += i * 100 + j

def printMap():
    output = ""
    for i in range(height):
        line = ""
        for j in range(width):
            line += map[i,j]
        output += line + "\n"
    print(output)

@functools.cache
def getDirectionCoords(direction):
    match direction:
        case '^':
            return 0, -1
        case 'v':
            return 0, 1
        case '<':
            return -1, 0
        case '>':
            return 1, 0
        case _:
            raise Exception("bruh")

def tryMoveInDirection(startX, startY, direction, allowMove = False):
    global currentPosition
    # see if there's something in front, try move that (recursively)
    # if there's a wall in front, return False
    # move up if all clear, return True

    char = map[startY, startX]

    dirX, dirY = getDirectionCoords(direction)
    nextX, nextY = startX + dirX, startY + dirY
    nextSpot = map[nextY, nextX]
    if nextSpot == '#':
        return False

    if nextSpot == '[':
        # it's the left of a box, try move it and the right side and all subsequent boxes
        if dirX == 0:
            if not (tryMoveInDirection(nextX, nextY, direction, allowMove) and tryMoveInDirection(nextX+1, nextY, direction, allowMove)):
                return False
        elif not tryMoveInDirection(nextX, nextY, direction, allowMove):
            return False
    elif nextSpot == ']':
        # it's the right of a box, try move it and the left side and all subsequent boxes
        if dirX == 0:
            if not (tryMoveInDirection(nextX, nextY, direction, allowMove) and tryMoveInDirection(nextX-1, nextY, direction, allowMove)):
                return False
        elif not tryMoveInDirection(nextX, nextY, direction, allowMove):
            return False
        
    # the robot and box(es) could move without hitting a wall
    if allowMove:
        map[nextY, nextX] = char
        map[startY, startX] = '.'
        currentPosition = (nextX, nextY)
    return True



with open("2024/15/input.txt") as f: 
    writingMap = True
    for i, line in enumerate(f):
        line = line.strip()
        if i == 0:
            height = int(len(line))
            width = height * 2

        if len(line) == 0:
            writingMap = False
        length = len(line)
        for j, char in enumerate(line):
            if writingMap:
                if char == '@':
                    currentPosition = startPosition = (j*2, i)
                    map[i,j*2] = '@'
                    map[i,j*2+1] = '.'
                elif char == 'O':
                    map[i,j*2] = '['
                    map[i,j*2+1] = ']'
                else:
                    map[i,j*2] = char
                    map[i,j*2+1] = char

            else:
                moves.append(char)

    printMap()
    
    for direction in moves:
        if tryMoveInDirection(currentPosition[0], currentPosition[1], direction):
            tryMoveInDirection(currentPosition[0], currentPosition[1], direction, True)

    calcGpsCoords()
    print(total)