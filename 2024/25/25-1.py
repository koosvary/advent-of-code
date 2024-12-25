
locks = []
keys = []

total = 0

def convertKeyToLock(heights):
    for i, result in enumerate(heights):
        heights[i] = 6 - result

    return heights

def testPins(key, lock):
    for i, bump in enumerate(key):
        if bump + lock[i] >= 6:
            return False
    return True

def testKeysInLocks():
    global total
    for key in keys:
        for lock in locks:
            if testPins(key, lock) is True:
                total += 1

with open('2024/25/input.txt') as f:
    current = []
    for i, line in enumerate(f):
        line = line.strip()
        
        if len(line) == 0:
            if isLock is True:
                locks.append(current)
            else:
                keys.append(current)

            print(current)
            continue

        if i % 8 == 0:
            current = [-1] * 5
            isLock = False if '.' in line else True

        for j, char in enumerate(line):
            if char == '#':
                current[j] += 1

    if isLock is True:
        locks.append(current)
    else:
        keys.append(current)

    testKeysInLocks()
    print(total)

    
            