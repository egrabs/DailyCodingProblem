# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, 
# and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Pre-condition: Root of BT must be non-null

def serialize(root):
	return seri_helper(root, '')
def seri_helper(node, BT_str):
	if node == None:
		# add a forward slash to indicate that the node doesn't exist -
		# the ordering of these tokens will indicate to the deserializer whether
		# it should create a right child or return out of the current recursive call
		BT_str = BT_str + '/ '
		return BT_str
	BT_str = (BT_str + str(node.val) + ' ')
	BT_str = seri_helper(node.left,  BT_str)
	BT_str = seri_helper(node.right, BT_str)
	return BT_str

def deserialize(BT_string):
	val_lst = BT_string.split(' ')
	root = Node(None)
	deseri_helper(val_lst, root)
	return root
def deseri_helper(values, node):
	node.val = values.pop(0)
	if values[0] != '/':
		node.left = Node(None)
		deseri_helper(values, node.left)
	else:
		values.pop(0)
	if values[0] != '/':
		node.right = Node(None)
		deseri_helper(values, node.right)
	else:
		values.pop(0)
	return

# The following test should pass:
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

#node = Node('One', Node('Two', Node('Three')), Node('Four', Node('Five')))
#s = serialize(node)
#tree = deserialize(s)
