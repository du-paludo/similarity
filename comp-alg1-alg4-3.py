import networkx as nx
import random
import time
import math

# O(len_u)
def similarity(sim1, u, v):
    neighbors_u = list(G.neighbors(u))  # O(len_u)
    # Como u e v não precisam ser vizinhos, remove da lista caso sejam
    if v in neighbors_u:
        neighbors_u.remove(v)   # O(1)
    len_u = len(neighbors_u)    # O(1)

    neighbors_v = list(G.neighbors(v))  # O(len_v)
    if u in neighbors_v:
        neighbors_v.remove(u)
    len_v = len(neighbors_v)

    common_neighbors = list(nx.common_neighbors(G, u, v))   # O(len_U)
    #return (w for w in G[u] if w in G[v] and w not in (u, v))

    len_common = len(common_neighbors)

    if (len_u + len_v - len_common) == 0:
        sim1[(u, v)] = 0
    else:
        sim1[(u, v)] = len_common / (len_u + len_v - len_common)


# -- Cria grafo --

n = 300
p = 0.3
G = nx.fast_gnp_random_graph(n, p)
#G = nx.gnp_random_graph(n, p)
#G = nx.powerlaw_cluster_graph(400, 30, 0.3)
#G = nx.complete_graph(500)
nodes = list(G.nodes)


# -- ALGORITMO 1 --

sim1 = {}

start_time = time.time()

for i in range(len(nodes)):     # O(n)
    for j in range(i + 1, len(nodes)):      # O(n)
        similarity(sim1, nodes[i], nodes[j])        # O(len_i)

print("Time of execution of algorithm 1: %s seconds" % (time.time() - start_time))


# -- ALGORITMO 2 --

sim2 = {}
for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        sim2[frozenset((i, j))] = [0, 0, 0]
signal_array = {}

start_time = time.time()

for node in nodes:      # O(n)
    for i in G.neighbors(node):     # O(len_neighbors)
        for j in random.choices(nodes, k=math.sqrt(n)):      # O(sqrt(n))       
        #for j in random.sample(nodes, k=math.sqrt(n)):      # O(sqrt(n))  
            if j == i or j == node or (frozenset((i, j)) in signal_array):
                continue
            if i in G.neighbors(node) and j in G.neighbors(node):       # O(len_neighbors)
                sim2[frozenset((i, j))][0] += 1                         # O(1)
            if i in G.neighbors(node) or j in G.neighbors(node):
                sim2[frozenset((i, j))][1] += 1
            signal_array[frozenset((i, j))] = 0
    signal_array.clear()    # O(len(signal_array))

print("Time of execution of algorithm 2: %s seconds" % (time.time() - start_time))

for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        if sim2[frozenset((i, j))][1] == 0:
            sim2[frozenset((i, j))] = 0
        else:
            sim2[frozenset((i, j))] = (sim2[frozenset((i, j))][0] / sim2[frozenset((i, j))][1])


# -- DIFERENÇAS --

sim_diff = {}

for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        sim_diff[(i, j)] = abs(sim2[frozenset((i, j))] - sim1[(i, j)])

diff_average = 0

for diff in sim_diff:
    diff_average += sim_diff[diff]

diff_average /= len(sim_diff)

print(diff_average)


# -- TESTES --

#print(sim1[(3, 5)])
#print(sim2[frozenset((3, 5))])