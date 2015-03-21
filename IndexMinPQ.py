__author__ = 'A88253'

from math import ceil

class IndexMinPQ:
    N = 0           # number of elements on PQ
    pq = []         # binary heap using 1-based indexing
    qp = []         # inverse: qp[pq[i]] = pq[qp[i]] = i
    keys = []       # items with priorities

    def __init__(self, maxN, type):
        self.keys = [None for i in range(0,maxN+1)]
        self.pq = [None for i in  range(0,maxN+1)]
        self.qp = [None for i in  range(0,maxN+1)]
        self.type = type
        for i in range(0,maxN+1): self.qp[i] = -1

    def isEmpty(self): return self.N == 0

    def contains(self, k):
        return self.qp[k] != -1

    def insert(self, k, key):
        self.N+=1
        self.qp[k] = self.N
        self.pq[self.N] = k
        self.keys[k] = key
        self.swim(self.N)

    def min(self):
        return self.keys[self.pq[1]]

    def delMin(self):
        indexOfMin = self.pq[1]
        self.exch(1, self.N)
        self.N -= 1
        self.sink(1, type)
        self.keys[self.pq[self.N+1]] = None
        self.qp[self.pq[self.N+1]] = -1
        return indexOfMin

    def greater(self, i, j):
        if self.type is "distance":
            return self.keys[self.pq[i]] > self.keys[self.pq[j]]
        elif self.type is "costs":
            return self.keys[self.pq[i]].costs > self.keys[self.pq[j]].costs
        elif self.type is "travelTime":
            return self.keys[self.pq[i]].travelTime > self.keys[self.pq[j]].travelTime

    def exch(self, i, j):
        t = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = t
        self.qp[self.pq[i]] = i
        self.qp[self.pq[j]] = j

    def swim(self, k):
        p = int(ceil(k/2.0))
        while k > 1 and self.greater(p, k):
            #print "exchanging node " + str(p) + " with node " + str(k)
            self.exch(p, k)
            k = p
            p = int(ceil(k/2.0))

    def sink(self, k, type):
        while 2*k <= self.N:
            j = 2 * k
            if j < self.N and self.greater(j, j+1): j += 1
            if not self.greater(k, j): break
            self.exch(k, j)
            k = j

    def change(self, k, key):
        self.keys[k] = key
        self.swim(self.qp[k]);
        self.sink(self.qp[k]);


#pq = IndexMinPQ(20)
#for i in range(0,20):
#    pq.insert(i,i)
#print pq.pq
#pq.change(0,100)
#print pq.pq
#print pq.min()