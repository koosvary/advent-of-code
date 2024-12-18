import sys
import networkx as nx
import matplotlib.pyplot as plt

testing = False
fewestSteps = sys.maxsize

def printGraph():
    pos = {point: point for point in map}
    fig, ax = plt.subplots()
    nx.draw(g, pos=pos, node_color='k', ax=ax)
    nx.draw(g, pos=pos, node_size=750, ax=ax, with_labels=True)  # draw nodes and edges
    ax.set_xlim(-1,width)
    ax.set_ylim(-1,height)
    ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
    plt.show()


if testing:
    width = height = 7
    input = '2024/18/testinput.txt'
    stopAt = 12
else:
    width = height = 71
    input = '2024/18/input.txt'
    stopAt = 1024

map = {}
fallingBytes = []

g = nx.Graph()
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for i in range(height):
    for j in range(width):
        map[i,j] = '.'
        g.add_node((i,j))

for node in map:
    x, y = node
    for direction in directions:
        dirX, dirY = direction
        neighbour = (x + dirX, y + dirY)
        if neighbour in map:
            g.add_edge(node, neighbour)

with open(input) as f:
    for i, line in enumerate(f):
        if i >= stopAt:
            break
        line = line.strip().split(',')
        corruptedNode = (int(line[0]), int(line[1]))
        fallingBytes.append(corruptedNode)
        g.remove_node(corruptedNode)

path = nx.shortest_path(g, (0,0), (width-1, height-1))

print(len(path) - 1) # don't count the last step, like the reindeer maze
    