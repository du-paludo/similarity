import networkx as nx

def similarity(G):
    S = {}
    for i in range(G.number_of_nodes()):
        for j in range(i + 1, G.number_of_nodes()):
            neighbors_i = list(G.neighbors(i))
            if j in neighbors_i:
                neighbors_i.remove(j)
            len_i = len(neighbors_i)

            neighbors_j = list(G.neighbors(j))
            if i in neighbors_j:
                neighbors_j.remove(i)
            len_j = len(neighbors_j)

            common_neighbors = list(nx.common_neighbors(G, i, j))
            len_common = len(common_neighbors)

            if (len_i + len_j - len_common) == 0:
                S[(i, j)] = 0
            else:
                S[(i, j)] = len_common / (len_i + len_j - len_common)
    return S

G = nx.fast_gnp_random_graph(5, 0.3)
S = similarity(G)