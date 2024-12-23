import networkx as nx

with open('2024/23/input.txt') as f:
    graph = nx.Graph()

    for line in f:
        line = line.strip()
        connections = line.split('-')
        graph.add_edge(connections[0], connections[1])

    cliques = list(nx.find_cliques(graph))
    biggestClique = sorted(max(cliques, key=len))

    print(','.join(biggestClique))