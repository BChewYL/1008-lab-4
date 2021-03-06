__author__ = 'Leonard'

import os
from Edge import Edge
from collections import deque
from EdgeWeightedGraph import EdgeWeightedGraph
from IndexMinPQ import IndexMinPQ
from DirectedEdge import DirectedEdge
import pygraphviz as pgv

class CableCarSystem:
    path = []
    marked = {}
    mst = deque()
    pq = None
    count = 0
    adjList = {} #dictonary

    ''' question 5c '''
    distTo = {}
    edgeTo = {}
    marked = {}
    ''' question 5c '''

    def __init__(self):
        graph = EdgeWeightedGraph()

    def readGraph(self, file):
        f = open(file, 'r')
        for line in f:
            v1, v2, v3, v4, v5 = line.split(" ")
            v1 = int(v1)
            v2 = int(v2)
            wt = float(v3)
            travelTimes = int(v4)
            costs = int(v5)

            e = Edge(v1, v2, wt, travelTimes, costs)

            if v1 in self.adjList:
                if self.isNeighbour(v1, v2) is False:
                    self.adjList[v1].append(e)
            else:
                self.adjList[v1]=[]
                self.adjList[v1].append(e)

            if v2 in self.adjList:
                if self.isNeighbour(v2, v1) is False:
                    self.adjList[v2].append(e)
            else:
                self.adjList[v2]=[]
                self.adjList[v2].append(e)

    def isNeighbour(self, v, w):
        for e in self.adjList[v]:
            if e.other(v) == w:
                return True
        return False

    def addEdge(self, v, w, wt):
        e = Edge(v, w, wt)

        if v in self.adjList:
            if self.isNeighbour(v, w) is False:
                self.adjList[v].append(e)
        else:
            self.adjList[v]=[]
            self.adjList[v].append(e)

        if w in self.adjList:
            if self.isNeighbour(w, v) is False:
                self.adjList[w].append(e)
        else:
            self.adjList[w] = []
            self.adjList[w].append(e)

    def adj(self, v):
        return self.adjList[v]

    def V(self):
        return self.adjList.keys()

    def E(self):
        edges = []
        for v in self.adjList:
            for e in self.adjList[v]:
                if e not in edges:
                    edges.append(e)
        return edges

    #prims algo
    def primsAlgo(self, type):
        self.pq = IndexMinPQ(len(self.E()), type)

        for v in self.V():
            self.marked[v] = False

        v = self.V()[0]
        count = 0
        self.visit(v)

        while not self.pq.isEmpty() and len(self.mst) < len(self.V())-1:
            e = self.pq.min()
            self.pq.delMin()
            v = e.either()
            w = e.other(v)
            if self.marked[v] and self.marked[w]: continue
            self.mst.append(e)
            if not self.marked[v]: self.visit(v)
            if not self.marked[w]: self.visit(w)

    #prims algo
    def visit(self, v):
        # mark v and add to pq all edges
        # from v to unmarked vertices
        self.marked[v] = True
        for e in self.adj(v):
            print "Visiting " + e.toString()
            if not self.marked[e.other(v)]:
                self.pq.insert(self.count, e)
                self.count += 1

    def edges(self):
        return self.mst

    def dijkstraAlgo(self, G, s, type):
        for v in G.V():
            self.marked[v] = False
            self.edgeTo[v] = None
            self.distTo[v] = float('Inf')

        self.pq = IndexMinPQ(len(G.V()), type)
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
            de = DirectedEdge(src,dest,e.weight, e.travelTime, e.costs)
            path.append(de)
            e = self.edgeTo[src]
            dest = src
        return path


    def createPath(self, v, w, weight, travelTimes, costs):
        e1 = Edge(v,w,weight, travelTimes, costs)
        self.path.append(e1)

    # draw the graph
    def drawGraph(self, filename, type):
        # create an empty undirected graph
        G = pgv.AGraph('graph myGraph {}')

        # draw edges
        for n in self.V():
            for e in self.adj(n):
                x = e.either()
                y = e.other(x)
                if type is "distance":
                    G.add_edge(x, y, e.weight, label=e.weight)
                elif type is "costs":
                    G.add_edge(x, y, e.costs, label=e.costs)
                elif type is "travelTime":
                    G.add_edge(x, y, e.travelTime, label=e.travelTime)

        #highlight edges in path with red color
        for e in self.path:
            v1 = e.either()
            v2 = e.other(v1)
            edge = G.get_edge(v1, v2)
            edge.attr['color']='red'

        # render graph into PNG file
        G.draw(filename,prog='dot')
        os.startfile(filename)


ccs = CableCarSystem()
ccs.readGraph("cablecar.txt")
type = "costs"    #question 5a - distance, question 5b - costs, question 5c - travelTime

if type is "distance" or type is "costs":
    ccs.primsAlgo(type)

    for e in ccs.edges():
        eV = e.either() #get left node
        eW = e.other(eV) #get right node
        ccs.createPath(eV, eW, e.weight, e.travelTime, e.costs)
    ccs.drawGraph("cablecargenerate.png", type)
elif type is "travelTime":
    s = ccs.V()[9]  #9 becos node 10 is in element [9]
    ccs.dijkstraAlgo(ccs, s, type)
    for v in ccs.V():
        print str(s) + " to " + str(v) + " (" + str(ccs.distTo[v]) + "):",
        for e in reversed(ccs.pathTo(7)):
            ccs.createPath(e.src(), e.dest(), e.weight, e.travelTime, e.costs)
            print str(e.src())+ "->" + str(e.dest()) + " " + str(e.weight) + " ",
        print
    ccs.drawGraph("cablecargenerate.png", type)
