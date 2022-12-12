import networkx as nx
import itertools
#import matplotlib.pyplot as plt

G = nx.fast_gnp_random_graph(300, 0.1)
#G = nx.cycle_graph(5)
nodes = list(G.nodes)

max_similarity = 0
min_similarity = 1
sum_similarity = 0
counter = 0

similarities = {}
for comb in itertools.combinations(nodes, 2):
    similarities[(comb[0], comb[1])] = [0, 0, 0]
    similarities[(comb[1], comb[0])] = [0, 0, 0]

for node in nodes:
    for i in G.neighbors(node):
        for j in nodes:
            if j == i or j == node:
                continue
            if similarities[(i, j)][2] == 1:
                continue
            if j in G.neighbors(node):
                similarities[(i, j)][0] += 1
            similarities[(i, j)][1] += 1
            similarities[(j, i)][2] = 1
            similarities[(i, j)][2] = 1
    for comb in itertools.combinations(nodes, 2):
        similarities[(comb[0], comb[1])][2] = 0
        similarities[(comb[1], comb[0])][2] = 0

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