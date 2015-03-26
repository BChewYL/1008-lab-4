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
    path = []

    def __init__(self, G, s):
        self.edgeTo = [None for i in range(0, len(G.V()))]
        self.distTo = [float('Inf') for i in range(0, len(G.V()))]
        self.distTo[s] = 0.0

        self.pq = IndexMinPQ(len(G.V()), type)
        self.distTo[s] = 0.0
        self.pq.insert(s, 0.0)
        for i in range(0, len(G.V())):
            for v in G.V():
                for e in G.adj(v):
                    #self.relax(e)
                    self.relax(v, e.other(v), e)

    def relax(self, v,w,e):
        #v = e.either()
        #w = e.other(v)
        if self.distTo[w] > self.distTo[v] + e.weight:
            self.distTo[w] = self.distTo[v] + e.weight
            self.edgeTo[w] = e

    def pathTo(self, v):
        path = []
        e = self.edgeTo[v]
        dest = v
        while e is not None:
            src = e.other(dest)
            de = DirectedEdge(src,dest,e.weight, 0, 0)
            path.append(de)
            e = self.edgeTo[src]
            dest = src
        return path

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

G = EdgeWeightedGraph()
G.readGraph("tinyEWG.txt")
s = G.V()[5]    #from node 5
sp = BellmanFordAlgo(G, s)
for v in G.V():
    print str(s) + " to " + str(v) + " (" + str(sp.distTo[v]) + "):",
    for e in reversed(sp.pathTo(6)):    #to node 6
        sp.createPath(e.src(), e.dest(), e.weight, 0, 0)
        print str(e.src())+ "->" + str(e.dest()) + " " + str(e.weight) + " ",
    print

sp.drawGraph("BellmanFord.png")
