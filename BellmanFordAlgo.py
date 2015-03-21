import os
from EdgeWeightedGraph import EdgeWeightedGraph
from Edge import Edge
from IndexMinPQ import IndexMinPQ
from DirectedEdge import DirectedEdge
import pygraphviz as pgv

class BellmanFordAlgo:

    distTo = []
    edgeTo = []
    pq = None

    def __init__(self, G, s):
        self.edgeTo = [None for i in range(0, len(G.V()))]
        self.distTo = [float('Inf') for i in range(0, len(G.V()))]
        self.distTo[s] = 0.0

        for i in range(0, len(G.V())):
            for v in G.V():
                for e in G.adj(v):
                    self.relax(e)

    def relax(self, e):
        v = e.either()
        w = e.other(v)
        if self.distTo[w] > self.distTo[v] + e.weight:
            self.distTo[w] = self.distTo[v] + e.weight
            self.edgeTo[w] = e

    def pathTo(self, v):
        path = []
        e = self.edgeTo[v]
        dest = v
        while e is not None:
            src = e.other(dest)
            de = DirectedEdge(src,dest,e.weight)
            path.append(de)
            e = self.edgeTo[src]
            dest = src
        return path

G = EdgeWeightedGraph()
G.readGraph("tinyEWG.txt")
s = G.V()[0]
sp = BellmanFordAlgo(G, s)
for v in G.V():
    print str(s) + " to " + str(v) + " (" + str(sp.distTo[v]) + "):",
    for e in reversed(sp.pathTo(v)):
        print str(e.src())+ "->" + str(e.dest()) + " " + str(e.weight) + " ",
    print
