import functools
map = {}
highestFound = 0
length = 0

@functools.cache
def findRoutes(point, previousValue):
    x, y = point

    if point not in map.keys():
        return 0

    valueAtPoint = map[point]

    if valueAtPoint != previousValue + 1:
        return 0

    if valueAtPoint == 9:
        return 1

    routesFound = 0
    routesFound += findRoutes((x + 1, y), valueAtPoint)
    routesFound += findRoutes((x - 1, y), valueAtPoint)
    routesFound += findRoutes((x, y + 1), valueAtPoint)
    routesFound += findRoutes((x, y - 1), valueAtPoint)
    return routesFound



with open("2024/10/input.txt") as f: 
    for i, line in enumerate(f):
        line = line.strip()
        length = len(line)
        for j, num in enumerate(line):
            map[i,j] = int(num)

    starts = [k for k,v in map.items() if v == 0]
    totalTrailheads = 0
    for startPoint in starts:
        trailheadsFound = findRoutes(startPoint, -1)
        totalTrailheads += trailheadsFound
    print(totalTrailheads)
        
        