
width = 0;
height = 0;

with open('2024/04/input.txt') as f:
    for line in f:
        width = len(line);
        height += 1;

stringToFind = 'XMAS'

def inBounds(number, length):
    if number < 0 or number >= length:
        return False;
    return True;

# Recursively find the string
def findIfContainsSubstring(fromX, fromY, xDir, yDir, substring):
    if len(substring) == 0:
        return True;

    global width, height;
    # ensure new spot isn't OoB
    newX = fromX + xDir;
    if not inBounds(newX, width):
        return False;
    newY = fromY + yDir;
    if not inBounds(newY, height):
        return False;

    if matrix[newX, newY] == substring[0]:
        return findIfContainsSubstring(newX, newY, xDir, yDir, substring[1:]);


matrix = {}
sequencesFound = 0;
with open('2024/04/input.txt') as f:
    for i, line in enumerate(f):
        for j, char in enumerate(line.strip()):
            matrix[i,j] = char;

for i in range(width):
    for j in range(height):
        if matrix[i,j] == stringToFind[0]:
            for xDir in range(-1,2):
                for yDir in range(-1,2):
                    if findIfContainsSubstring(i,j, xDir, yDir, stringToFind[1:]):
                        sequencesFound += 1;

print(sequencesFound);