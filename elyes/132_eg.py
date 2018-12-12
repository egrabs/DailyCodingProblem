# Design and implement a HitCounter class that keeps track of requests (or hits). It should support the following operations:

# record(timestamp): records a hit that happened at timestamp
# total(): returns the total number of hits recorded
# range(lower, upper): returns the number of hits that occurred between timestamps lower and upper (inclusive)

class HitCounter:
    def __init__(self):
        self.hits = []

    def record(self, timestamp):
        idx = 0
        for i in range(len(self.hits)):
            if self.hits[i] > timestamp:
                idx = i
                break
        self.hits.insert(idx, timestamp)


    def total(self):
        return len(self.hits)

    def range(self, lower, upper):
        count = 0
        for timestamp in self.hits:
            if timestamp >= lower and timestamp <= upper:
                count += 1
            if timestamp > upper:
                # since they're stored in sorted order
                break
        return count