width = height = 0
map = {}

def printMap():
    output = ""
    for i in range(height):
        line = ""
        for j in range(width):
            line += map[j,i]
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

# the number of edges should be the same as the number of corners in the shape
# this assertion should be true even if a region is wholly wrapping another
# say it's wrapping a square, that would just add 4 edges due to the squares 4 corners
# will need to get a mechanism for both interior and exterior facing corners
def findCorners(region):
    corners = 0
    for node in region:
        testedNodes = set()
        char = map[node]
        # if both neighbours are not this node's value, that's an exterior corner
        # else, using pairs neighbour nodes: if both match, have those neighbours check the shared cell that isn't this node
        # if that cell is different, that's an interior corner

        x, y = node
        # do left + top/bottom, the right + top/bottom
        topAndBottom = leftAndRight = [-1, 1]

        for lr in leftAndRight:
            dirX = lr
            lr = (x + lr, y)
            for tb in topAndBottom:
                dirY = tb
                tb = (x, y + tb)
                # if one's OoB and one's in, if the one that's in is different value,
                # we have an internal corner
                if lr not in map and tb not in map:
                    #corner of the map
                    corners += 1
                    continue

                if lr in map and tb not in map:
                    if map[lr] != map[node]:
                        corners += 1
                    continue
                elif lr not in map and tb in map:
                    if map[tb] != map[node]:
                        corners += 1
                    continue

                # we know they're in bounds due to checks above
                if tb in region and lr in region:
                    diagonal = (x + dirX, y + dirY)
                    if diagonal not in testedNodes and map[diagonal] != map[node]:
                        testedNodes.add(diagonal)
                        # external corner
                        corners += 1
                elif tb not in region and lr not in region:
                    #internal corner
                    corners += 1
    return corners

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
            map[j,i] = char

printMap()

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
            edges = findCorners(newRegion)
            cost = area * edges
            totalCost += cost
            print(f'{map[list(newRegion)[0]]}: {cost}')

print(totalCost)