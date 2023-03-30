import networkx as nx
import itertools
import random

# -- Cria grafo --
G = nx.fast_gnp_random_graph(300, 0.1)
#G = nx.complete_graph(5)
nodes = list(G.nodes)

# -- Inicializa variáveis --
max_similarity = 0
min_similarity = 1
sum_similarity = 0
counter = 0

# -- Inicializa dicionário que guarda similaridades --
similarities = {}
for comb in itertools.combinations(nodes, 2):
    similarities[comb] = [0, 0, 0]

# -- Algoritmo --
for node in nodes:
    for i in G.neighbors(node):
        for j in random.choices(nodes, k=10):
            if i < j:
                menor = i
                maior = j
            else:
                menor = j
                maior = i
            if j == i or j == node or similarities[(menor, maior)][2] == 1:
                continue
            if j in G.neighbors(node):
                similarities[(menor, maior)][0] += 1
            similarities[(menor, maior)][1] += 1
            similarities[(menor, maior)][2] = 1
    for comb in itertools.combinations(nodes, 2):
        similarities[comb][2] = 0

# -- Calcula similaridades --
for comb in itertools.combinations(nodes, 2):
    if similarities[comb][1] == 0:
        continue
    sim = similarities[comb][0] / similarities[comb][1]
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