import networkx as nx
#import matplotlib.pyplot as plt

def similarity(u, v):
    neighbors_u = list(G.neighbors(u))
    # Como u e v não precisam ser vizinhos, remove da lista caso sejam
    if v in neighbors_u:
        neighbors_u.remove(v)
    len_u = len(neighbors_u)

    neighbors_v = list(G.neighbors(v))
    if u in neighbors_v:
        neighbors_v.remove(u)
    len_v = len(neighbors_v)

    common_neighbors = list(nx.common_neighbors(G, u, v))
    len_common = len(common_neighbors)

    sim = len_common/(len_u + len_v - len_common)

    return sim

# Cria um grafo
G = nx.fast_gnp_random_graph(300, 0.1)
#G = nx.complete_graph(200)

nodes = list(G.nodes)
#print("List of nodes in graph:", nodes)
#print("")

max_similarity = 0
min_similarity = 1
sum_similarity = 0
counter = 0

for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        sim = similarity(nodes[i], nodes[j])
        if sim < min_similarity:
            min_similarity = sim
        elif sim > max_similarity:
            max_similarity = sim
        sum_similarity += sim
        counter += 1

average_similarity = sum_similarity/counter

print("Maximum similarity:", max_similarity)
print("Minimum similarity:", min_similarity)
print("Average similarity:", average_similarity)

#nx.draw(G)
#plt.show()