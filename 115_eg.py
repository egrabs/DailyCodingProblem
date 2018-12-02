# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s.
# A subtree of s is a tree consists of a node in s and all of this node's descendants.
# The tree s could also be considered as a subtree of itself.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSubtreeOf(t, s):
    # checks whether t is a subtree of s
    def checkSubtree(t, s):
        if t.val != s.val or (t.left and not s.left) or (not t.left and s.left) or (t.right and not s.right) or (not t.right and s.right):
            return False
        if t.left and t.right:
            return checkSubtree(t.left, s.left) and checkSubtree(t.right, s.right)
        elif t.left:
            return checkSubtree(t.left, s.left)
        elif t.right:
            return checkSubtree(t.right, s.right)
        return True

    if checkSubtree(t, s):
        return True

    if s.left and s.right:
        return isSubtreeOf(t, s.left) or isSubtreeOf(t, s.right)
    elif s.left:
        return isSubtreeOf(t, s.left)
    elif s.right:
        return isSubtreeOf(t, s.right)
    else:
        return False

t_1 = Node(1)
t_3 = Node(3)
t_root = Node(2, t_1, t_3)

    # t
      #   2
      #  / \
      # 1   3


s_2_l = Node(2)
s_1 = Node(1)
s_3 = Node(3)
s_2_r = Node(2, s_1, s_3)
s_root = Node(5, s_2_l, s_2_r)

    # s
        #   5
        #  / \
        # 2   2
        #    / \
        #   1   3

print isSubtreeOf(t_root, s_root) == True

t_3.left = Node(7)
t_3.right = Node(8)

    # t
      #   2
      #  / \
      # 1   3
      #    / \
      #   7   8

print isSubtreeOf(t_root, s_root) == False

s_3.left = Node(7)
s_3.right = Node(8)

    # s
        #   5
        #  / \
        # 2   2
        #    / \
        #   1   3
        #      / \  
        #     7   8

print isSubtreeOf(t_root, s_root) == True

s_3.left.left = Node(10)

    # s
        #   5
        #  / \
        # 2   2
        #    / \
        #   1   3
        #      / \  
        #     7   8
        #    /
        #   10

print isSubtreeOf(t_root, s_root) == False


