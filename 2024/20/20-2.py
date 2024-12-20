import networkx as nx

map = set()
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

testing = False

minimumStepsSaved = 50 if testing else 100
picosecondsCheatable = 20
totalGoodCheats = 0

filename = 'testinput' if testing else 'input'

with open(f'2024/20/{filename}.txt') as f:
    g = nx.DiGraph()
    for j, line in enumerate(f):
        line = line.strip()
        for i, char in enumerate(line):
            if char == '#':
                continue
            if char == 'E':
                e = (i, j)
            if char == 'S':
                s = (i, j) # reindeer starts pointing west

            map.add((i,j))
            
for node in map:
    x, y = node
    for direction in directions:
        dirX, dirY = direction
        neighbour = (x + dirX, y + dirY)
        
        if neighbour in map: 
            g.add_edge(node, neighbour, weight=1)


shortestPath = nx.shortest_path(g, s, e, weight='weight')


def getCheatEndpoints(coords):
    i, j = coords
    output = set()
    for distanceX in range(-picosecondsCheatable, picosecondsCheatable + 1):
        distanceYMax = picosecondsCheatable - abs(distanceX)
        for distanceY in range(-distanceYMax, distanceYMax + 1):
            if (i + distanceX, j + distanceY) in shortestPath:
                output.add((i + distanceX, j + distanceY))
    return output

for i, node in enumerate(shortestPath):
    potentialCheatNodes = getCheatEndpoints(node)
    for potentialCheat in potentialCheatNodes:
        j = shortestPath.index(potentialCheat)

        manhattanDistance = abs(node[0] - potentialCheat[0]) + abs(node[1] - potentialCheat[1])

        stepsSaved = j - i - manhattanDistance
        if stepsSaved < minimumStepsSaved:
            continue 

        totalGoodCheats += 1

print(totalGoodCheats)