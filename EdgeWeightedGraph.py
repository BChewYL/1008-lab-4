__author__ = 'A88253'

from Edge import Edge

class EdgeWeightedGraph:

    adjList = {} #dictonary

    def readGraph(self, file):
        f = open(file, 'r')
        for line in f:
            v1, v2, v3 = line.split(" ")
            v1 = int(v1)
            v2 = int(v2)
            wt = float(v3)

            e = Edge(v1, v2, wt)

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




