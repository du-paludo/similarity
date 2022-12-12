import networkx as nx
import itertools
import random
import time

def similarity(similarities1, u, v):
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

    similarities1[(u, v)][0] = len_common
    similarities1[(u, v)][1] = len_u + len_v - len_common
    sim = similarities1[(u, v)][0]/similarities1[(u, v)][1]

    return sim

# -- Cria grafo --
G = nx.fast_gnp_random_graph(300, 0.3)
#G = nx.complete_graph(200)
nodes = list(G.nodes)


# -- ALGORITMO 1 --

similarities1 = {}
for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        similarities1[(i, j)] = [0, 0]

sum_similarity = 0
counter = 0

start_time = time.time()

for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        sum_similarity += similarity(similarities1, nodes[i], nodes[j])
        counter += 1

average_similarity = sum_similarity/counter
print("Average similarity in algorithm 1:", average_similarity)
print("Time of execution of algorithm 1: %s seconds" % (time.time() - start_time))


# -- ALGORITMO 4 --

sum_similarity = 0
counter = 0

similarities4 = {}
for comb in itertools.combinations(nodes, 2):
    similarities4[comb] = [0, 0, 0]

start_time = time.time()

for node in nodes:
    for i in G.neighbors(node):
        for j in random.choices(nodes, k=200):
            if i < j:
                menor = i
                maior = j
            else:
                menor = j
                maior = i
            if j == i or j == node or similarities4[(menor, maior)][2] == 1:
                continue
            if j in G.neighbors(node):
                similarities4[(menor, maior)][0] += 1
            similarities4[(menor, maior)][1] += 1
            similarities4[(menor, maior)][2] = 1
    for comb in itertools.combinations(nodes, 2):
        similarities4[comb][2] = 0

for comb in itertools.combinations(nodes, 2):
    if similarities4[comb][1] == 0:
        continue
    sim = similarities4[comb][0] / similarities4[comb][1]
    sum_similarity += sim
    counter += 1

average_similarity = sum_similarity/counter

print("Average similarity in algorithm 2:", average_similarity)
print("Time of execution of algorithm 2: %s seconds" % (time.time() - start_time))


# -- TESTES --

print(similarities1[3, 5][0] / similarities1[3, 5][1])
print(similarities4[3, 5][0] / similarities4[3, 5][1])