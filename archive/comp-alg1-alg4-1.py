import networkx as nx
import itertools
import random
import time

def similarity(sim1, u, v):
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

    if (len_u + len_v - len_common) == 0:
        sim1[(u, v)] = 0
    else:
        sim1[(u, v)] = len_common / (len_u + len_v - len_common)


# -- Cria grafo --
G = nx.fast_gnp_random_graph(300, 0.3)
#G = nx.complete_graph(200)
nodes = list(G.nodes)


# -- ALGORITMO 1 --

sim1 = {}

start_time = time.time()

for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        similarity(sim1, nodes[i], nodes[j])

print("Time of execution of algorithm 1: %s seconds" % (time.time() - start_time))


# -- ALGORITMO 4 --

sum_similarity = 0
counter = 0

sim2 = {}
for comb in itertools.combinations(nodes, 2):
    sim2[comb] = [0, 0, 0]

start_time = time.time()

for node in nodes:
    for i in G.neighbors(node):
        #for j in random.choices(nodes, k=30):
        for j in random.sample(nodes, k=300):
            if i < j:
                menor = i
                maior = j
            else:
                menor = j
                maior = i
            if j == i or j == node or sim2[(menor, maior)][2] == 1:
                continue
            if j in G.neighbors(node):
                sim2[(menor, maior)][0] += 1
            sim2[(menor, maior)][1] += 1
            sim2[(menor, maior)][2] = 1
    for comb in itertools.combinations(nodes, 2):
        sim2[comb][2] = 0

for comb in itertools.combinations(nodes, 2):
    if sim2[comb][1] == 0:
        sim2[comb] = 0
    else:
        sim2[comb] = sim2[comb][0] / sim2[comb][1]

print("Time of execution of algorithm 2: %s seconds" % (time.time() - start_time))


# -- DIFERENÇAS --

sim_diff = {}

for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        sim_diff[(i, j)] = abs(sim2[(i, j)] - sim1[(i, j)])

diff_average = 0

for diff in sim_diff:
    diff_average += sim_diff[diff]

diff_average /= len(sim_diff)

print(diff_average)


# -- TESTES --

#print(sim1[3, 5] / sim1[3, 5])
#print(sim2[3, 5] / sim2[3, 5])