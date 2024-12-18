import networkx as nx
import matplotlib.pyplot as plt

testing = False
wantToPrint = False

def printGraph(filename, path = None):
    if not wantToPrint:
        return
    
    pos = {point: point for point in map}
    fig, ax = plt.subplots()
    inches = width if testing else 30 # max 3000x3000px
    fig.set_size_inches(inches, inches)
    nx.draw(g, pos=pos, node_color='k', ax=ax)
    nx.draw(g, pos=pos, ax=ax, with_labels=testing, font_weight='bold')  # draw nodes and edges
    ax.set_xlim(-1,width)
    ax.set_ylim(-1,height)
    if path is not None:
        path_edges = list(zip(path,path[1:]))
        nx.draw_networkx_nodes(g, pos, nodelist=path, node_color='r')
        nx.draw_networkx_edges(g, pos, edgelist=path_edges, edge_color='r')
    ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)

    if filename is not None:
        prefix = 'test_' if testing else ''
        plt.savefig(f'2024/18/screenshots/{prefix}img_{str(filename+1).zfill(4)}.png', format='PNG', bbox_inches='tight')
    plt.close()


if testing:
    width = height = 7
    input = '2024/18/testinput.txt'
else:
    width = height = 71
    input = '2024/18/input.txt'

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
        line = line.strip().split(',')
        corruptedNode = (int(line[0]), int(line[1]))
        fallingBytes.append(corruptedNode)

for i, corruptedNode in enumerate(fallingBytes):
    try:
        path = nx.shortest_path(g, (0,0), (width-1, height-1))
        printGraph(i, path)
    except:
        printGraph(i, None)
        print(fallingBytes[i-1])
        break
    
    g.remove_node(corruptedNode)