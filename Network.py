__author__ = 'A88253'

import os
from EdgeWeightedGraph import EdgeWeightedGraph
import pygraphviz as pgv
from Edge import Edge
from collections import deque

class Network:
    graph = EdgeWeightedGraph()
    path = []

    def __init__(self):
        graph = EdgeWeightedGraph()

    def readGraph(self, filename):
        f = open(filename, 'r')
        for line in f:
            v1, v2, v3 = line.split(" ")
            weight = float(v3)
            self.graph.addEdge(v1, v2, weight)

    def createPath(self):
        e1 = Edge("A","B",0.0)
        e2 = Edge("B","C",0.0)
        self.path.append(e1)
        self.path.append(e2)

    # draw the graph
    def drawGraph(self, filename):
        # create an empty undirected graph
        G = pgv.AGraph('graph myGraph {}')

        # draw edges
        for n in self.graph.V():
            for e in self.graph.adj(n):
                x = e.either()
                y = e.other(x)
                G.add_edge(x, y, e.weight, label=e.weight)

        #highlight edges in path with red color
        for e in self.path:
            v1 = e.either()
            v2 = e.other(v1)
            edge = G.get_edge(v1, v2)
            edge.attr['color']='red'

        # render graph into PNG file
        G.draw(filename,prog='dot')
        os.startfile(filename)

nw = Network()
nw.readGraph("demo.txt")
nw.createPath()
nw.drawGraph("demo.png")