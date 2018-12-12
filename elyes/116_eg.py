# Generate a finite, but an arbitrarily large binary tree quickly in O(1).

# That is, generate() should return a tree whose size is unbounded but finite.

import random as rand

class InfiniteNode:
    def __init__(self, val)
        self.left = None
        self.right = None

    def getLeft():
        if self.left is None:
            self.left = InfiniteNode(rand.random())
        return self.left

    def getRight():
        if self.right is None:
            self.right = InfiniteNode(rand.random())
        return self.right


def generate():
    return InfiniteNode(rand.random())