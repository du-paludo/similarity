import networkx as nx
import matplotlib.pyplot as plt

def similarity(u, v):
    neighbors_u = list(G.neighbors(u))
    # Como u e v não precisam ser vizinhos, remove da lista caso sejam
    if v in neighbors_u:
        neighbors_u.remove(v)

    len_u = len(neighbors_u)
    #print("All neighbors of node u:", neighbors_u)
    #print("Number of neighbors of node u:", len_u)
    #print("")

    neighbors_v = list(G.neighbors(v))
    if u in neighbors_v:
        neighbors_v.remove(u)

    len_v = len(neighbors_v)
    #print("All neighbors of node v:", neighbors_v)
    #print("Number of neighbors of node v:", len_v)
    #print("")

    common_neighbors = list(nx.common_neighbors(G, u, v))
    len_common = len(common_neighbors)
    #print("Common neighbors between u and v:", common_neighbors)
    #print("Number of common neighbors between u and v:", len_common)
    #print("")

    sim = len_common/(len_u + len_v - len_common)
    #print("Similarity =", sim)

    return sim

G = nx.cycle_graph(4)

nodes = list(G.nodes)
print()
print("List of nodes in graph:", nodes)
print("")

max_similarity = 0
min_similarity = 1
sum_similarity = 0
counter = 0

for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        #print(nodes[i], nodes[j])
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

nx.draw(G)
plt.show()