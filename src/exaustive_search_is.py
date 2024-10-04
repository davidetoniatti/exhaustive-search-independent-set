#!/usr/bin/env python3

import random as rd
from utils import *
import sys


def expandProblem(P, G):
    P2 = (P[0][1:], P[1][:])
    candidate = P[0][0]
    for nodo in list(G.neighbors(candidate)):
        if nodo in P[0]:
            P[0].remove(nodo)
    P1 = (P[0][1:], P[1][:])
    P1[1].append(candidate)
    return [P1, P2]


def get_max_is_branchAndBound(G):
    """
    Exaustive search algorithm
    """
    S = [(list(G.nodes), [])]
    bestSoFar = []
    while len(S) != 0:
        problem = S.pop(rd.randrange(len(S)))
        subProblems = expandProblem(problem, G)
        for prob in subProblems:
            newsol = prob[0] + prob[1]
            if isIndependentSet(G, prob[0]):
                if len(bestSoFar) < len(newsol):
                    bestSoFar = newsol
            elif len(bestSoFar) <= len(newsol):
                S.append(prob)
    return bestSoFar


if __name__ == "__main__":
    G, n, m = generate_graph_from_file(sys.argv[1])
    write_independent_set_to_file(get_max_is_branchAndBound(G))
