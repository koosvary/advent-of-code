import networkx as nx

directions = (1, -1, 1j, -1j) # use imaginary numbers for east<->west

with open('2024/16/input.txt') as f:
    g = nx.DiGraph()
    for i, line in enumerate(f):
        line = line.strip()
        for j, char in enumerate(line):
            if char == '#':
                continue
            node = i + 1j * j

            if char == 'E':
                e = node
            if char == 'S':
                s = (node, 1j) # reindeer starts pointing west
            
            for nodeDir in directions:
                g.add_node((node, nodeDir))
            
    for node, nodeDir in g.nodes:
        if (node + nodeDir, nodeDir) in g.nodes:
            # orthogonally connected in the same direction as previous node
            # eg, connect node A's north direction with node B's north
            # no need to connect A's north to B's south - it'd be redundant
            g.add_edge((node, nodeDir), (node + nodeDir, nodeDir), weight=1)
        for rotation in -1j, 1j:
            # connect 90 degree corners
            # using i, since i**2 = 1 so it'll respect a turn
            g.add_edge((node, nodeDir), (node, nodeDir * rotation), weight=1000)

    # need to make a new endpoint otherwise the exit will not be found
    for direction in directions:
        # we appear to have an off-by-one problem, remove the last move to the exit
        g.add_edge((e, direction), 'end', weight=0)

    # very thankful for NetworkX
    allShortestPaths = nx.all_shortest_paths(g, s, 'end', weight='weight')
    
    seats = {
        node
        for path in allShortestPaths
        for node, _ in path[:-1]
    }

    print(seats)
    print(len(seats))
    