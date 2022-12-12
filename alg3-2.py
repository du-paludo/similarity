import networkx as nx
import itertools

G = nx.cycle_graph(100)
nodes = list(G.nodes)

max_similarity = 0
min_similarity = 1
sum_similarity = 0
counter = 0

similarities = {}
for comb in itertools.combinations(nodes, 2):
    similarities[comb] = [0, 0]

for node in nodes:
    for comb in itertools.combinations(nodes, 2):
        i = comb[0]
        j = comb[1]
        if i == node or j == node:
            continue
        if i in G.neighbors(node) and j in G.neighbors(node):
            similarities[comb][0] += 1
        if i in G.neighbors(node) or j in G.neighbors(node):
            similarities[comb][1] += 1

for comb in itertools.combinations(nodes, 2):
    sim = similarities[comb][0] / similarities[comb][1]
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