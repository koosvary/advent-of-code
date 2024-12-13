map = {}
highestFound = 0
length = 0

peaks= {}

def findRoutes(point, previousValue):
    global peaks
    x, y = point

    if point not in map.keys():
        return

    valueAtPoint = map[point]

    if valueAtPoint != previousValue + 1:
        return

    if valueAtPoint == 9:
        peaks[point] = True
        return

    findRoutes((x + 1, y), valueAtPoint)
    findRoutes((x - 1, y), valueAtPoint)
    findRoutes((x, y + 1), valueAtPoint)
    findRoutes((x, y - 1), valueAtPoint)



with open("2024/10/input.txt") as f: 
    for i, line in enumerate(f):
        line = line.strip()
        length = len(line)
        for j, num in enumerate(line):
            map[i,j] = int(num)

    starts = [k for k,v in map.items() if v == 0]
    totalTrailheads = 0
    for startPoint in starts:
        findRoutes(startPoint, -1)
        totalTrailheads += len(peaks)
        peaks = {}
    print(totalTrailheads)
        
        