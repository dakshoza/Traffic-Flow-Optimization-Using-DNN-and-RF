import networkx as nx

G = nx.Graph()
G.add_edges_from([(0,"I1"),(1,"I1"), (2, "I1"), ("I1", "I2"), ("I2", 3), ("I2", 4),("I2", 5)])

def getPath(start, end):
    return nx.shortest_path(G,start,end)