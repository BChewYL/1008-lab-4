__author__ = 'A88253'

class Edge:
    v = None # vertex 1
    w = None # vertex 2
    weight = None # weight

    #travelTime and costs added becos question 5
    def __init__(self, v, w, wt, travelTime, costs):
        self.v = v
        self.w = w
        self.weight = wt

        ''' question 5 '''
        self.travelTime = travelTime
        self.costs = costs
        ''' question 5 '''

    # return either endpoint
    def either(self):
        return self.v

    # return the other endpoint
    def other(self, v):
        if v==self.v:
            return self.w
        else:
            return self.v

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

    #travelTime and costs added becos question 5
    def toString(self):
        return str(self.v) + "-" + \
               str(self.w) + " weight/distance: " + \
               str(self.weight) + " travel times: " + \
               str(self.travelTime) + " costs: " + \
               str(self.costs)



