__author__ = 'A88253'

import os
from EdgeWeightedGraph import EdgeWeightedGraph
from Edge import Edge
from IndexMinPQ import IndexMinPQ
from DirectedEdge import DirectedEdge
import pygraphviz as pgv

class DijkstraSP:
    distTo = {}
    edgeTo = {}
    marked = {}
    pq = None
    path = []

    def __init__(self, G, s):
        for v in G.V():
            self.marked[v] = False
            self.edgeTo[v] = None
            self.distTo[v] = float('Inf')

        self.pq = IndexMinPQ(len(G.V()))
        self.distTo[s] = 0.0
        self.pq.insert(s, 0.0)
        while not self.pq.isEmpty():
            v = self.pq.delMin()
            self.marked[v] = True
            #print "Relaxing vertex " + str(v)
            for e in G.adj(v):
                self.relax(v, e.other(v), e)

    def relax(self, v, w, e):
        if self.distTo[w] > self.distTo[v] + e.weight:
            self.distTo[w] = self.distTo[v] + e.weight
            self.edgeTo[w] = e
            if self.pq.contains(w):
                self.pq.change(w, self.distTo[w])
            elif self.marked[w] is False:
                self.pq.insert(w, self.distTo[w])

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

    def createPath(self, v, w, weight):
         e1 = Edge(v,w,weight)
         self.path.append(e1)

    def drawGraph(self, filename):
        Gpgv = pgv.AGraph('graph myGraph {}')
        for n in G.V():
            for e in G.adj(n):
                x = e.either()
                y = e.other(x)
                Gpgv.add_edge(x, y, e.weight, label=e.weight)

        for e in self.path:
            v1 = e.either()
            v2 = e.other(v1)
            edge = Gpgv.get_edge(v1, v2)
            edge.attr['color']='red'

        Gpgv.draw(filename,prog='dot')
        os.startfile(filename)

G = EdgeWeightedGraph()
G.readGraph("tinyEWG.txt")
s = G.V()[0]
sp = DijkstraSP(G, s)
for v in G.V():
    print str(s) + " to " + str(v) + " (" + str(sp.distTo[v]) + "):",
    for e in reversed(sp.pathTo(v)):
        sp.createPath(e.src(), e.dest(), e.weight)
        print str(e.src())+ "->" + str(e.dest()) + " " + str(e.weight) + " ",
    print

filename="dijkstragenerate.png"
sp.drawGraph(filename)