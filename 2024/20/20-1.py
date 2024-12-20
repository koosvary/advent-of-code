import networkx as nx

map = set()
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

minimumStepsSaved = 100
picosecondsCheatable = 2
totalGoodCheats = 0

with open('2024/20/input.txt') as f:
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

    print(shortestPath)

    # new idea since brute force blows
    # try find nodes with manhattan distance of 2, subtract the steps between these two points
    # the time saved should be this subpath's distance, no?
    for i, node in enumerate(shortestPath):
        for j, otherNode in enumerate(shortestPath):
            if i > j or node == otherNode:
                continue

            manhattanDistance = abs(node[0] - otherNode[0]) + abs(node[1] - otherNode[1])

            if 2 <= manhattanDistance <= picosecondsCheatable:
                newPath = shortestPath[:i+1] + shortestPath[j-1:] # gotta keep the start and end in the original path
                stepsSaved = len(shortestPath) - len(newPath)
                if stepsSaved >= minimumStepsSaved:
                    totalGoodCheats += 1

print(totalGoodCheats)