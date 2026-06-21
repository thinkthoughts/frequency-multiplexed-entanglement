import networkx as nx

def pair_graph(n_pairs):
    G = nx.Graph()
    for i in range(1, n_pairs + 1):
        G.add_edge(-i, i)
    return G
