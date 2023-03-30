import networkx as nx
import itertools
import random

# -- Cria grafo --
G = nx.fast_gnp_random_graph(300, 0.1)
#G = nx.powerlaw_cluster_graph(400, 30, 0.3)
#G = nx.cycle_graph(10)
nodes = list(G.nodes)

# -- Inicializa variáveis --
max_similarity = 0
min_similarity = 1
sum_similarity = 0
counter = 0

# -- Inicializa dicionário que guarda similaridades --
similarities = {}
for comb in itertools.combinations(nodes, 2):
    similarities[frozenset(comb)] = [0, 0, 0]

# -- Algoritmo --
for node in nodes:
    for i in G.neighbors(node):
        for j in random.choices(nodes, k=50):
            if j == i or j == node or similarities[frozenset((i, j))][2] == 1:
                continue
            if j in G.neighbors(node):
                similarities[frozenset((i, j))][0] += 1
            similarities[frozenset((i, j))][1] += 1
            similarities[frozenset((i, j))][2] = 1
    for comb in itertools.combinations(nodes, 2):
        similarities[frozenset(comb)][2] = 0

# -- Calcula similaridades --
for comb in itertools.combinations(nodes, 2):
    if comb[0] == comb[1]:
        continue
    sim = similarities[frozenset(comb)][0] / similarities[frozenset(comb)][1] 
    if sim < min_similarity:
        min_similarity = sim
    elif sim > max_similarity:
        max_similarity = sim
    sum_similarity += sim
    counter += 1
average_similarity = sum_similarity/counter

# -- Imprime resultados --
print("Maximum similarity:", max_similarity)
print("Minimum similarity:", min_similarity)
print("Average similarity:", average_similarity)