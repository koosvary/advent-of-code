width = 0;
height = 0;

with open('2024/04/input.txt') as f:
    for line in f:
        width = len(line);
        height += 1;

charsToFind = [];

def resetCharsToFind():
    global charsToFind;
    charsToFind = ['M', 'S'];

def inBounds(number, length):
    if number < 0 or number >= length:
        return False;
    return True;

def cornerIsGood(xPos, yPos):
    global charsToFind;
    global width, height;

    if not (inBounds(xPos, width) and inBounds(yPos, height)):
        return False;

    charAtPoint = matrix[xPos, yPos]
    if charAtPoint in charsToFind:
        return True;

# Recursively find the string
def charHasGoodDiagonal(xPos, yPos, xDir, yDir):
    global charsToFind;
    resetCharsToFind();

    # ensure new spot isn't OoB
    cornerX = xPos + xDir;
    cornerY = yPos + yDir;

    if cornerIsGood(cornerX, cornerY):
        charsToFind.remove(matrix[cornerX, cornerY]);
        
        cornerX = xPos + (xDir * -1);
        cornerY = yPos + (yDir * -1);

        if cornerIsGood(cornerX, cornerY):
            return True;
    return False;


matrix = {}
crossesFound = 0;
with open('2024/04/input.txt') as f:
    for i, line in enumerate(f):
        for j, char in enumerate(line.strip()):
            matrix[i,j] = char;

for i in range(width):
    for j in range(height):
        if matrix[i,j] == 'A':
            if charHasGoodDiagonal(i, j, -1, -1) and charHasGoodDiagonal(i, j, 1, -1):
                crossesFound += 1;

print(crossesFound);