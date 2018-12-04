
# Implement a bit array.

# A bit array is a space efficient array that holds a value of 1 or 0 at each index.

# init(size): initialize the array with size
# set(i, val): updates index at i with val where val is either 1 or 0.
# get(i): gets the value at index i.

import math

class BitArray:
    def __init__(self, size):
        self.size = size
        numInts = int(math.ceil(size / 32.))
        self.ints = [int(0) for _ in range(numInts)]

    def set(self, i, val):
        if i >= self.size:
            raise ValueError('Index out of bounds!')
        if val != 1 and val != 0:
            raise ValueError('Value to set must be 1 or 0')
        intInd = int(math.floor(i / 32.))
        bitInd = i % 32
        mask = 1 << bitInd
        if val == 0:
            mask = ~mask
            self.ints[intInd] = mask & self.ints[intInd]
        else:
            self.ints[intInd] = mask | self.ints[intInd]

    def get(self, i):
        if i >= self.size:
            raise ValueError('Index out of bounds!')
        intInd = int(math.floor(i / 32.))
        bitInd = i % 32
        return (self.ints[intInd] >> bitInd) & 1

arr = BitArray(75)

arr.set(72, 1)

print arr.get(72)

arr.set(72, 0)

print arr.get(72)

print arr.get(64)

