import networkx as nx
import math
import random

def similarity_estimation(G):
    S = {}
    for i in range(G.number_of_nodes()):
        for j in range(i + 1, G.number_of_nodes()):
            S[frozenset((i, j))] = [0, 0]
    signal_array = {}

    for node in range(G.number_of_nodes()):
        for i in G.neighbors(node):
            for j in random.sample(list(G.nodes), k=int(math.sqrt(G.number_of_nodes()))):  
                if j == i or j == node or (frozenset((i, j)) in signal_array):
                    continue
                if i in G.neighbors(node) and j in G.neighbors(node):
                    S[frozenset((i, j))][0] += 1
                if i in G.neighbors(node) or j in G.neighbors(node):
                    S[frozenset((i, j))][1] += 1
                signal_array[frozenset((i, j))] = 0
        signal_array.clear()

    for i in range(G.number_of_nodes()):
        for j in range(i + 1, G.number_of_nodes()):
            if S[frozenset((i, j))][1] == 0:
                S[frozenset((i, j))] = 0
            else:
                S[frozenset((i, j))] = (S[frozenset((i, j))][0] / S[frozenset((i, j))][1])
    
    return S

G = nx.fast_gnp_random_graph(5, 0.3)
S = similarity_estimation(G)