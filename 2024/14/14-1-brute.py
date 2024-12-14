import re

testing = False # change this when doing the actual input
seconds = 100

tiles = []

def quadrantSafetyScore(startRow, endRow, startCol, endCol):
    sum = 0
    for i in range(startRow, endRow):
        for j in range(startCol, endCol):
            sum += tiles[i][j]
    return sum    

def move(position, velocity, secondsToGo):
    if secondsToGo == 0:
        return
   
    pX, pY = position
    vX, vY = velocity

    newPosX = (pX + vX) % width
    newPosY = (pY + vY) % height

    tiles[pY][pX] -= 1
    tiles[newPosY][newPosX] += 1

    move((newPosX,newPosY), velocity, secondsToGo - 1)

match testing:
    case True:
        inputPath = "2024/14/testinput.txt"
        width = 11
        height = 7
    case False:
        inputPath = "2024/14/input.txt"
        width = 101
        height = 103

for i in range(height):
    tiles.append([])
    for j in range(width):
        tiles[i].append(0);


with open(inputPath) as f: 
    for line in f:
        line = line.strip()

        regex = re.findall(r"(-*\d+)", line)
        
        startPosition = (int(regex[0]), int(regex[1]))
        velocity = (int(regex[2]), int(regex[3]))
        
        pX, pY = startPosition
        tiles[pY][pX] += 1
        move(startPosition, velocity, seconds)

middleRow = int(height / 2)
middleCol = int(width / 2)

q1 = quadrantSafetyScore(0, middleRow, 0, middleCol)
q2 = quadrantSafetyScore(0, middleRow, middleCol + 1, width)
q3 = quadrantSafetyScore(middleRow + 1, height, 0, middleCol)
q4 = quadrantSafetyScore(middleRow + 1, height, middleCol + 1, width)

print(q1 * q2 * q3 * q4)