currentValue = 0;
fileArray = [];
total = 0;

def createBlockArray(line):
    global currentValue
    for i, char in enumerate(line):
        freeSpace = i % 2 == 1;

        if freeSpace:
            for _ in range(int(char)):
                fileArray.append(".")
        else:
            for _ in range(int(char)):
                fileArray.append(currentValue)
            currentValue += 1

def sortfileString():
    global fileString;
    while True:
        firstDotIndex = next((idx, space) for idx, space in enumerate(fileArray) if str(space) == ".")[0]
        lastCharIndex = next((idx, space) for idx, space in enumerate(fileArray[::-1]) if str(space) != ".")[0]
        lastCharIndex = len(fileArray) - lastCharIndex - 1
        if firstDotIndex > lastCharIndex:
            break
        fileArray[firstDotIndex] = fileArray[lastCharIndex]
        fileArray[lastCharIndex] = "."

def checksum():
    global total;
    counter = 0;
    for i, char in enumerate(fileArray):
        if char == ".":
            return
        total += counter * int(char)
        counter += 1

with open("2024/09/input.txt") as f: 
    for line in f:
        createBlockArray(line)
        sortfileString()
        checksum()
        print(total)