from collections import deque
from UnionFind import UnionFind
from EdgeWeightedGraph import EdgeWeightedGraph
from IndexMinPQ import IndexMinPQ

''' question 3b '''

class KruskalAlgo:

    mst = deque()

    def __init__(self, G, type):

        #build priority queue
        print len(G.E())
        pq = IndexMinPQ(len(G.E()), type)

        #sort edges
        for e in G.E():
            pq.insert(pq.N, e)

        uf = UnionFind(len(G.V()))

        while not pq.isEmpty() and len(self.mst) < len(G.V())-1:
            e = pq.min() #delete min operation. greedily add edge with smallest weight to MST
            print "minimum edge " + e.toString()
            pq.delMin()
            v = e.either()
            w = e.other(v)

            if not uf.connected(v, w):  #edge v-w does not create cycle
                uf.union(v, w)  #merge sets
                self.mst.append(e)  #add edge to MST

    def edges(self):
        return self.mst


G = EdgeWeightedGraph()
G.readGraph("tinyEWG.txt")
type = "distance"
mst = KruskalAlgo(G, type)
sum = 0
for e in mst.edges():
    print e.toString()
    sum += e.weight

print sum