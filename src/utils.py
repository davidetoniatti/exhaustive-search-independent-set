#!/usr/bin/env python3

import networkx as nx
from itertools import combinations, chain


def random_graph_generator(n, p):
    G = nx.gnp_random_graph(n, p, seed=None, directed=False)
    fname = "input.txt"
    with open(fname, "w") as f:
        f.write(f"{len(list(G.nodes))} {len(list(G.edges))}\n")
        for e in G.edges:
            f.write(f"{e[0]} {e[1]}\n")


def generate_graph_from_file(fname="input.txt"):
    """
    Given an input file, it returns a graph G with n nodes and m edges.
    """
    G = nx.Graph()

    with open(fname, "r") as f:
        edge_list = f.read().splitlines().split(" ")
        n, m = edge_list[0].split(" ")

    for e in edge_list[1:]:
        (u, v) = e.split(" ")
        u, v = int(u), int(v)
        G.add_nodes_from([u, v])
        G.add_edge(u, v)

    return G, n, m


def isIndependentSet(G, nodelist):
    """
    Given a graph G and a list of nodes nodelist, it checks if
    nodelist is an independent set for G.
    """
    for u in nodelist:
        for v in G.neighbors(u):
            if v in nodelist:
                return False
    return True


def write_independent_set_to_file(iset, fname="output.txt"):
    """
    Given a list of nodes, it writes the list of nodes to a file.
    """
    with open(fname, "w") as f:
        f.write(str(len(iset)) + "\n")
        for node in iset:
            f.write(str(node) + "\n")


def degMinNode(G):
    """
    Given a graph G, it returns the node of G with the minimum degree.
    """
    min = len(G.nodes) + 1
    node = None
    for u in G.nodes():
        l = len(list(G.neighbors(u)))
        if l < min:
            min = l
            node = u
    return node
