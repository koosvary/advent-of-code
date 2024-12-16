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
            if map[i,j] == 'O':
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

def tryMoveInDirection(startX, startY, direction):
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

    if nextSpot == 'O':
        # it's a box, try move it and all subsequent boxes
        if not tryMoveInDirection(nextX, nextY, direction):
            return False
        
    # the robot and box(es) could move without hitting a wall
    map[nextY, nextX] = char
    map[startY, startX] = '.'
    currentPosition = (nextX, nextY)
    return True



with open("2024/15/input.txt") as f: 
    writingMap = True
    for i, line in enumerate(f):
        line = line.strip()
        if i == 0:
            width = height = int(len(line))

        if len(line) == 0:
            writingMap = False
        length = len(line)
        for j, char in enumerate(line):
            if writingMap:
                if char == "@":
                    currentPosition = startPosition = (j, i)
                map[i,j] = char
            else:
                moves.append(char)

    printMap()

    for direction in moves:
        tryMoveInDirection(currentPosition[0], currentPosition[1], direction)

    printMap()
    calcGpsCoords()
    print(total)