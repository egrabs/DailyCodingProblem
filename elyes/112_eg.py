# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# Assume that each node in the tree also has a pointer to its parent.

# According to the definition of LCA on Wikipedia:
# "The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as
# descendants (where we allow a node to be a descendant of itself)."

class Node(object):
    def __init__(self, val, parent=None, left=None, right=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right


def LCA(node1, node2):
    if node1 == node2:
        return node1

    def hasChild(start, toFind):
        if (start == None):
            return False
        if (start == toFind):
            return True
        return hasChild(start.left, toFind) or hasChild(start.right, toFind)

    node1Parent = node1.parent
    node1Depth = 0
    while node1Parent != None:
        node1Depth += 1
        node1Parent = node1Parent.parent

    node2Parent = node2.parent
    node2Depth = 0
    while node2Parent != None:
        node2Depth += 1
        node2Parent = node2Parent.parent

    # early exit if one of the nodes is root
    # because it is clearly ancestor of everything
    if node1Depth == 0:
        return node1
    if node2Depth == 0:
        return node2

    startNode = node1 if node1Depth > node2Depth else node2
    findNode = node2 if node1Depth > node2Depth else node1

    while startNode != None:
        if hasChild(startNode, findNode):
            return startNode
        startNode = startNode.parent

    return None

fifteen = Node(15)
sixteen = Node(15, left=fifteen)
fifteen.parent = sixteen
thirteen = Node(13)
fourteen = Node(14, left=thirteen, right=sixteen)
thirteen.parent = fourteen
sixteen.parent = fourteen
three = Node(3)
six = Node(6)
five = Node(5, left=three, right=six)
three.parent = five
six.parent = five
ten = Node(10, left=five, right=fourteen)
fourteen.parent = ten
five.parent = ten

       #      10
       #    /    \
       #   5     14
       #  / \   /  \
       # 3   6 13  16
       #          /
       #         15

print(LCA(thirteen, fifteen) == fourteen)
print(LCA(five, five) == five)
print(LCA(ten, sixteen) == ten)
print(LCA(three, fourteen) == ten)
print(LCA(six, three) == five)
