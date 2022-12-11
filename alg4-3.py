import networkx as nx
import itertools
import random
#import matplotlib.pyplot as plt

#G = nx.fast_gnp_random_graph(300, 0.1)
G = nx.cycle_graph(4)
nodes = list(G.nodes)

max_similarity = 0
min_similarity = 1
sum_similarity = 0
counter = 0

similarities = {}
for comb in itertools.combinations(nodes, 2):
    print(comb)
    similarities[frozenset(comb)] = [0, 0, 0]
    print(similarities[frozenset(comb)])

print(similarities)

for node in nodes:
    for i in G.neighbors(node):
        for j in random.choices(nodes, k=8):
            if j == i or j == node:
                continue
            print(similarities[frozenset((i, j))])
            print(i, j)
            if similarities[frozenset((i, j))][2] == 1:
                continue
            if j in G.neighbors(node):
                similarities[frozenset((i, j))][0] += 1
            similarities[frozenset((i, j))][1] += 1
            similarities[frozenset((i, j))][2] = 1
    for comb in itertools.combinations(nodes, 2):
        similarities[frozenset(comb)] = 0

for comb in itertools.combinations(nodes, 2):
    sim = (similarities[(comb[0], comb[1])][0] + similarities[(comb[1], comb[0])][0]) / (similarities[(comb[0], comb[1])][1] + similarities[(comb[1], comb[0])][1])
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