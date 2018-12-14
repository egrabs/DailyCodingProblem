# Given a binary tree, return all paths from the root to leaves.

# For example, given the tree

#    1
#   / \
#  2   3
#     / \
#    4   5
# it should return [[1, 2], [1, 3, 4], [1, 3, 5]].

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def allPaths(root):
    paths = []
    def recurse(n, path=[]):
        if n.left:
            recurse(n.left, path + [n.val])
        if n.right:
            recurse(n.right, path + [n.val])
        if not n.left and not n.right:
            paths.append(path + [n.val])
    recurse(root)
    return paths


five = Node(5)
four = Node(4)
three = Node(3, left=four, right=five)
two = Node(2)
one = Node(1, left=two, right=three)

print(allPaths(one))