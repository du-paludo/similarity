import networkx as nx
import matplotlib.pyplot as plt
import random
import time
import math

# O(len_u)
def similarity(G, sim1, u, v):
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


def diff_calc(n, p, y1, y2):
    # -- Cria grafo --

    G = nx.fast_gnp_random_graph(n, p)
    nodes = list(G.nodes)


    # -- ALGORITMO 1 --

    sim1 = {}

    start_time = time.time()

    for i in range(len(nodes)):     # O(n)
        for j in range(i + 1, len(nodes)):      # O(n)
            similarity(G, sim1, nodes[i], nodes[j])        # O(len_i)

    execution_time = time.time() - start_time
    print("Time of execution of algorithm 1: %s seconds" % (time.time() - start_time))
    y1.append(execution_time)


    # -- ALGORITMO 2 --

    sim2 = {}
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            sim2[frozenset((i, j))] = [0, 0, 0]
    signal_array = {}

    start_time = time.time()

    for node in nodes:      # O(n)
        for i in G.neighbors(node):     # O(len_neighbors)
            for j in random.sample(nodes, k=int(math.sqrt(n))):      # O(sqrt(n))       
                if j == i or j == node or (frozenset((i, j)) in signal_array):
                    continue
                if i in G.neighbors(node) and j in G.neighbors(node):       # O(len_neighbors)
                    sim2[frozenset((i, j))][0] += 1                         # O(1)
                if i in G.neighbors(node) or j in G.neighbors(node):
                    sim2[frozenset((i, j))][1] += 1
                signal_array[frozenset((i, j))] = 0
        signal_array.clear()    # O(len(signal_array))

    execution_time = time.time() - start_time
    print("Time of execution of algorithm 2: %s seconds" %(execution_time))
    y2.append(execution_time)

    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            if sim2[frozenset((i, j))][1] == 0:
                sim2[frozenset((i, j))] = 0
            else:
                sim2[frozenset((i, j))] = (sim2[frozenset((i, j))][0] / sim2[frozenset((i, j))][1])


    # -- DIFERENÇAS --

    sim_diff = {}
    average_sim1 = 0
    average_sim2 = 0
    counter = 0

    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            average_sim1 += sim1[(i, j)]
            average_sim2 += sim2[frozenset((i, j))]
            sim_diff[(i, j)] = abs(sim2[frozenset((i, j))] - sim1[(i, j)])
            counter += 1

    average_sim1 /= counter
    average_sim2 /= counter

    print("Average similarity of algorithm 1:", average_sim1)
    print("Average similarity of algorithm 2:", average_sim2)

    diff_average = 0

    for diff in sim_diff:
        diff_average += sim_diff[diff]

    diff_average /= len(sim_diff)

    print("Average difference between algorithms:", diff_average)

    print("Percentage of average difference and exact similarity:", diff_average/average_sim1)


# -- EXECUTA TESTES --

x1 = []
x2 = []
y1 = []
y2 = []
p = 0.1
for i in range(200, 1001, 200):
    print("For n =", i)
    x1.append(i)
    x2.append(i)
    diff_calc(i, p, y1, y2)
    print("")

# -- GERA GRÁFICO --

plt.plot(x1, y1, label = "Algorithm 1")
plt.plot(x2, y2, label = "Algorithm 2")
plt.xlabel("Graph size (n)")
plt.ylabel("Time of execution")
plt.title("Comparing with probability 0.3")
plt.legend()
plt.show()