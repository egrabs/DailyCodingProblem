# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, 
# and deserialize(s), which deserializes the string back into the tree.

import pdb

# For example, given the following Node class
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    return serializeHelper(root,'')

def serializeHelper(node,treetext):
    if node==None:
        treetext = treetext + '; '
        return treetext
    treetext = treetext + str(node.val) + ' '
    treetext = serializeHelper(node.left,treetext)
    treetext = serializeHelper(node.right,treetext)
    return treetext

def deserialize(treetext):
    val_list = treetext.split(' ')
    root = Node(None, val_list.pop(0))
    return deserializeHelper(val_list,root)

def deserializeHelper(val_list,root,next_val):
    if not val_list:
        return None
    if val_list[0] == ';':
        return None
    #pdb.set_trace()
    root.left = deserializeHelper(val_list,root,val_list.pop(0))
    root.right = deserializeHelper(val_list,root,val_list.pop(0))
    return root

node = Node('One', Node('Two', Node('Three')), Node('Four', Node('Five')))
s = serialize(node)
print s
deserialize(s)
