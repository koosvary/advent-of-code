width = height = 0
map = {}

def printMap():
    output = ""
    for i in range(height):
        line = ""
        for j in range(width):
            line += map[i,j]
        output += line + "\n"
    print(output)

def findNeighbours(node):
    x, y = node
    nodes = set()
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for direction in directions:
        dirX, dirY = direction
        neighbour = (x + dirX, y + dirY)
        if neighbour in map:
            nodes.add(neighbour)
    return nodes

def findFences(region):
    totalFences = 0
    for node in region:
        neighbours = findNeighbours(node)
        fences = 4 - len(neighbours)
        for candidate in neighbours:
            if candidate not in region:
                # there's a fence between the candidate
                fences += 1

        totalFences += fences
    return totalFences

def getRegion(node):
    region = set() # set is like dict but I don't have to do that stupid (x,y): True thing I was doing
    checkedNodes = set()
    # do BFS or something
    uncheckedNeighbours = [node]
    while len(uncheckedNeighbours) != 0:
        node = uncheckedNeighbours[0]
        region.add(node)
        checkedNodes.add(node)
        # get neighbours
        # add them to list if they have the same character

        neighbourCandidates = findNeighbours(node)
        unvisitedNeighbours = [neighbour for neighbour in neighbourCandidates if (map[neighbour] == map[node] and neighbour not in checkedNodes and neighbour not in uncheckedNeighbours)]
        uncheckedNeighbours += unvisitedNeighbours
        del uncheckedNeighbours[0]
        
    return region

with open("2024/12/input.txt") as f:
    for i, line in enumerate(f):
        line = line.strip()
        if i == 0:
            width = height = int(len(line))
        for j, char in enumerate(line):
            map[i,j] = char

printMap()

# ideas
# don't actually put fences up, it'll be a nightmare
# for each area, recursively crawl across a spot for area, add them to a 2D list
# find orthogonally adjacent neighbours for each of these spots
# fencesAtSpot = 4 - neighbours
# pray.

visitedNodes = set()
regions = []
totalCost = 0

for i in range(height):
    for j in range(width):
        node = (i, j)
        if node not in visitedNodes:
            # region finding
            newRegion = getRegion(node)
            regions.append(newRegion)
            visitedNodes |= newRegion

            # costs
            area = len(newRegion)
            perimeter = findFences(newRegion)
            cost = area * perimeter
            totalCost += cost
            print(f'{map[list(newRegion)[0]]}: {cost}')

print(totalCost)