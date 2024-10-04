#!/usr/bin/env python3

from utils import *
import sys


def greedyIS(graph):
    """
    Algoritmo greedy non ottimale
    """
    G = graph.copy()
    S = []
    while G.number_of_nodes() != 0:
        v = degMinNode(G)
        S.append(v)
        G.remove_nodes_from(list(G.neighbors(v)) + [v])
    return S


if __name__ == "__main__":
    G, n, m = generate_graph_from_file(sys.argv[1])
    write_independent_set_to_file(greedyIS(G))
