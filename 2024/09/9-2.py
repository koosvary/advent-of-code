import re

currentValue = 0
fileArray = []
total = 0
numbersInserted = {}

def printFileStorage():
    print("".join(fileArray).replace("-", ""))


def concatNeighbouringPeriodBlocks():
    global fileArray
    index = 0
    while True:
        if index+1 == len(fileArray):
            return

        leftBlock = fileArray[index]
        rightBlock = fileArray[index+1]

        if "." in leftBlock:
            if "." in rightBlock:
                fileArray[index] += fileArray[index+1]
                del fileArray[index+1]
            else:
                index += 1
        else:
            index += 1


def createBlockArray(line):
    global currentValue
    for i, char in enumerate(line):
        freeSpace = i % 2 == 1

        if freeSpace:
            if int(char) != 0:
                fileArray.append("." * int(char))
        else:
            # It'll be difficult to know whether a block is 9, 99 or 9999, for example
            # Adding a hyphen after every number will let us use it as a delimiter later
            fileArray.append((str(currentValue) + "-") * int(char))
            numbersInserted[currentValue] = int(char)
            currentValue += 1

def sortFileArray():
    global fileArray
    lastUsedIndex = -1
    uniqueDigits = currentValue - 1
    
    for digit in range(uniqueDigits, -1, -1):
        # Starting at the end, find numeric block locations
        # Find the first available spot for it 
        # If no spot, move on - only try to move things once
        for i, blockToMove in enumerate(reversed(fileArray)):
            if "." in blockToMove:
                continue

            blockDigit = int(blockToMove.split("-")[0])
            if digit != blockDigit:
                continue

            blockTrueSize = numbersInserted[digit]
            lastUsedIndex = i
            break

        blockToMoveIndex = len(fileArray) - lastUsedIndex
        for j in range(blockToMoveIndex):
            emptySpaceBlock = fileArray[j]
            if "." not in emptySpaceBlock:
                continue
            
            spaceAvailable = len(emptySpaceBlock)
            if blockTrueSize == spaceAvailable:
                # overwrite then delete the original block to shrink the list
                fileArray[j] = blockToMove
                fileArray[blockToMoveIndex - 1] = "." * spaceAvailable
                break
            elif blockTrueSize < spaceAvailable:
                # gotta make sure we respect the remaining empty space
                spaceRemaining = spaceAvailable - blockTrueSize
                spaceUsed = spaceAvailable - spaceRemaining
                fileArray[blockToMoveIndex - 1] = "." * spaceUsed
                fileArray[j] = "." * spaceRemaining
                fileArray.insert(j, blockToMove)
                break
        concatNeighbouringPeriodBlocks()

def checksum():
    global total
    counter = 0

    for block in fileArray:
        if "." in block:
            # Dots get skipped, but the counter does still increase, apparently
            counter += len(block)

        numbers = re.findall(r"(\d+\-)", block)
        numbers = [int(number.replace("-", "")) for number in numbers]
        for number in numbers:
            sum = counter * number
            total += sum
            counter += 1

with open("2024/09/input.txt") as f: 
    for line in f:
        createBlockArray(line)
        printFileStorage()
        sortFileArray()
        printFileStorage()
        checksum()
        print(total)