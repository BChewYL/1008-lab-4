__author__ = 'A88253'

import os
from Edge import Edge
from collections import deque
from EdgeWeightedGraph import EdgeWeightedGraph
from IndexMinPQ import IndexMinPQ
import pygraphviz as pgv

class PrimMST:
    marked = {}
    mst = deque()
    pq = None
    count = 0
    path = []

    def __init__(self, G, type):
        self.pq = IndexMinPQ(len(G.E()), type)

        for v in G.V():
            self.marked[v] = False

        v = G.V()[0]
        count = 0
        self.visit(G,v)

        while not self.pq.isEmpty() and len(self.mst) < len(G.V())-1:
            e = self.pq.min()
            self.pq.delMin()
            v = e.either()
            w = e.other(v)
            if self.marked[v] and self.marked[w]: continue
            self.mst.append(e)
            if not self.marked[v]: self.visit(G,v)
            if not self.marked[w]: self.visit(G,w)

    def visit(self, G, v):
        # mark v and add to pq all edges
        # from v to unmarked vertices
        self.marked[v] = True
        for e in G.adj(v):
            print "Visiting " + e.toString()
            if not self.marked[e.other(v)]:
                self.pq.insert(self.count, e)
                self.count += 1

    def edges(self):
        return self.mst

    ''' start question 3a '''
    #travelTime and costs added becos question 5
    def createPath(self, v, w, weight, travelTime, costs):
        e1 = Edge(v,w,weight, travelTime, costs)
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
    ''' end question 3a '''


G = EdgeWeightedGraph()
G.readGraph("tinyEWG.txt")
mst = PrimMST(G, "distance")
sum = 0

for e in mst.edges():
    eV = e.either() #get left node
    eW = e.other(eV)    #get right node
    mst.createPath(eV, eW, e.weight, 0, 0)
    print e.toString()
    sum += e.weight

filename="primgenerate.png"
mst.drawGraph(filename)

print sum
