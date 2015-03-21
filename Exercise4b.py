import os
from EdgeWeightedGraph import EdgeWeightedGraph
from Edge import Edge
from IndexMinPQ import IndexMinPQ
from DirectedEdge import DirectedEdge
import pygraphviz as pgv

class Question4b:
    graph = EdgeWeightedGraph()
    storeEdges = []
    def __init__(self):
        graph = EdgeWeightedGraph()

    def readGraph(self, filename, nodeName, nodeWeight):
        f = open(filename, 'r')
        for line in f:
            v1, v2, v3 = line.split(" ")
            weight = float(v3)
            self.graph.addEdge(v1, v2, weight)

        self.getVerticesFromEither(nodeName)
        self.displayVerticesAndDistance(nodeWeight, nodeName)

    def getVerticesFromEither(self, nodeName):

        for e in self.graph.adj(nodeName):
            x = e.either()
            y = e.other(x)
            if x is nodeName:
                self.storeEdges.append(e)
            elif y is nodeName:
                self.storeEdges.append(e)

    def displayVerticesAndDistance(self, edgeWeight, nodeName):
        for x in range(0, len(self.storeEdges)):
            if self.storeEdges[x].weight < edgeWeight:
                if nodeName is self.storeEdges[x].v:
                    print "node: "+str(self.storeEdges[x].w),
                    print " weight: "+str(self.storeEdges[x].weight)
                if nodeName is self.storeEdges[x].w:
                    print "node: "+str(self.storeEdges[x].v),
                    print " weight: "+str(self.storeEdges[x].weight)
                #print "start node: "+str(self.storeEdges[x].v),
                #print " end node: "+str(self.storeEdges[x].w),
                #print " weight: "+str(self.storeEdges[x].weight)
q4b = Question4b()
q4b.readGraph("tinyEWG.txt", "5", 0.36)