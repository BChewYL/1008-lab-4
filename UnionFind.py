__author__ = 'A88253'

class UnionFind:
    id = []       # access to component id
    count = None  # number of components

    def __init__(self, N):  # initialize component id array
        self.count = N
        self.id = [i for i in range(0,N)]

    def union(self, p, q):
        pID = self.find(p)
        qID = self.find(q)

        # nothing to do if p and q are already
        # in the same component
        if pID == qID: return

        for i in range(0, len(self.id)):
            if self.id[i] == pID:
                self.id[i] = qID

        self.count -= 1

    def find(self, p):
        return self.id[p]

    def connected(self, p, q):
        return self.find(p) == self.find(q)


