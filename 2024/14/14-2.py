import re
import cv2
import numpy as np

testing = False # change this when doing the actual input

xPosition = []
yPosition = []
xVelocity = []
yVelocity = []

def quadrantSafetyScore(startRow, endRow, startCol, endCol):
    sum = 0
    for i in range(startRow, endRow):
        for j in range(startCol, endCol):
            sum += tiles[i][j]
    return sum

match testing:
    case True:
        inputPath = "2024/14/testinput.txt"
        width = 11
        height = 7
    case False:
        inputPath = "2024/14/input.txt"
        width = 101
        height = 103

# numpy arrays can be made into pngs with openCV
tiles = np.zeros((height, width), dtype=np.int64)

with open(inputPath) as f: 
    for i, line in enumerate(f):
        line = line.strip()

        pX, pY, vX, vY = map(int, re.findall(r"(-*\d+)", line))

        xPosition.append(pX)
        yPosition.append(pY)
        xVelocity.append(vX)
        yVelocity.append(vY)
        tiles[pY, pX] = 1


numRobots = len(xPosition)
# Run this thing 10000 times and save them to PNGs.
# I'm not crazy, you're crazy
for i in range(10000):
    for robot in range(numRobots):
        pX = xPosition[robot]
        pY = yPosition[robot]
        vX = xVelocity[robot]
        vY = yVelocity[robot]

        newPosX = (pX + vX) % width
        newPosY = (pY + vY) % height

        xPosition[robot] = newPosX
        yPosition[robot] = newPosY

        tiles[pY, pX] -= 1
        tiles[newPosY, newPosX] += 1

    tilesForImage = np.copy(tiles)

    # Gotta make all the squares with bots be 255 otherwise OpenCV will make a heatmap
    # Without this you'll see hotspots but never see the tree
    tilesForImage[tilesForImage > 0] = 255

    cv2.imwrite(f"2024/14/screenshots/img_{str(i+1).zfill(4)}.png", tilesForImage) # imwrite(filename, img[, params])
