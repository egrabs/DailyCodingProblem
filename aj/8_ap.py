# A unival tree (which stands for "universal value") is a tree where all nodes
# under it have the same value.

# Given the root to a binary tree, count the number of unival subtrees.

# For example, the following tree has 5 unival subtrees:

#   0
#  / \
# 1   0
#    / \
#   1   0
#  / \
# 1   1

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Create same tree pictured above for testing
tst_root = Node(0,Node(1),Node(0,Node(1,Node(1),Node(1)),Node(0)))

def count_univals(root):
    results = unival_help(root)
    return results[1]

def unival_help(node):
    if node == None:
        return(True, 0)

    # Traverse the tree in post-order
    ancestor_info_L = unival_help(node.left)
    ancestor_info_R = unival_help(node.right)

    # This evaluates to True iif the currently observed node is 
    # the root of a unival subtree
    if (ancestor_info_L[0] and ancestor_info_R[0]) \
    and (node.left == None or node.val == node.left.val) \
    and (node.right == None or node.val == node.right.val):
        return(True, ancestor_info_L[1] + ancestor_info_R[1] + 1)
    else:
        return (False, ancestor_info_L[1] + ancestor_info_R[1])

# Should be O(n) time and O(1) space, w/ n = #nodes 

print(count_univals(tst_root) == 5)