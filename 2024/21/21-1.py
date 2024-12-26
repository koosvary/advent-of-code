import re

def makeKeypad(rows):
    coords = {}
    gap = '0,0' if len(rows) == 2 else '3,0'
    
    for i, row in enumerate(rows):
        for j, key in enumerate(row):
            if key == ' ':
                continue

            coords[key] = (i,j)
    
    return (coords, gap)

# using a networkx graph for shortest paths between numbers worked well in theory
# but unfortunately led to some issues due to how many corners appeared.
# for example, 3 to 7 could be done by <<^^, but could also be <^<^, which has
# extra movements for the second robot and onwards.
def moveToKey(fromKey, toKey, keypad):
    coords, keypadGap = keypad

    [r1, c1] = coords[fromKey]
    [r2, c2] = coords[toKey]

    rowDifference = r2 - r1
    upDown = ('v' if r2 > r1 else '^') * abs(rowDifference)

    colDifference = c2 - c1
    leftRight = ('>' if c2 > c1 else '<') * abs(colDifference)

    if (c2 > c1 and f'{r2},{c1}' != keypadGap):
        return f'{upDown}{leftRight}A'
    
    if (f'{r1},{c2}' != keypadGap):
        return f'{leftRight}{upDown}A'

    return f'{upDown}{leftRight}A'

arrowKeypadsNeeded = 2
total = 0
with open('2024/21/input.txt') as f:
    for line in f:
        line = line.strip()
        numericPart = int(re.search(r'(\d+)', line).group(0))

        
        # first arrow keypad robot's steps
        numpadKeys = makeKeypad(["789", "456", "123", " 0A"])
        previous = 'A'
        path = ''
        for i, char in enumerate(line):
            path += moveToKey(previous, char, numpadKeys)
            previous = char
        print (path)

        # second through to last arrow pad robot's codes
        arrowKeys = makeKeypad([' ^A', '<v>'])
        previous = 'A'
        for _ in range(arrowKeypadsNeeded):
            newPath = ''
            for i, char in enumerate(path):
                newPath += moveToKey(previous, char, arrowKeys)
                previous = char
            print (newPath)
            path = newPath

        totalInputs = len(path)
        print('total inputs:', totalInputs)

        complexity = totalInputs * numericPart
        print(f'{line}: {totalInputs} * {numericPart} = {complexity}')

        total += complexity

    print(total)


