__author__ = 'A88253'

class DirectedEdge:
    v = None # source vertex
    w = None # destination vertex
    weight = None # weight

    def __init__(self, v, w, wt, travelTime, costs):
        self.v = v
        self.w = w
        self.weight = wt
        self.travelTime = travelTime
        self.costs = costs

    def src(self):
        return self.v

    def dest(self):
        return self.w

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __ge__(self, other):
        return self.weight >= other.weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def toString(self):
        return str(self.v) + "-" + \
               str(self.w) + " " + \
               str(self.weight)


