import networkx as nx
import itertools
#import matplotlib.pyplot as plt

G = nx.cycle_graph(4)
nodes = list(G.nodes)
#print("List of nodes in graph:", nodes)
#print("")

max_similarity = 0
min_similarity = 1
sum_similarity = 0
counter = 0

similarities = []
number_nodes = len(nodes)
for i in range(number_nodes):
    col = []
    for j in range(number_nodes):
        col.append([0., 0.])
    similarities.append(col)

for node in nodes:
    for comb in itertools.combinations(nodes, 2):
        i = comb[0]
        j = comb[1]
        print(comb)
        if i == node or j == node:
            continue
        if i in G.neighbors(node) and j in G.neighbors(node):
            similarities[i][j][0] += 1
        if i in G.neighbors(node) or j in G.neighbors(node):
            similarities[i][j][1] += 1
        print(i, j, similarities[i][j])
    print("")

for row in similarities:
    print(row)
print("")

for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        sim = similarities[i][j][0] / similarities[i][j][1]
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