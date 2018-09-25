# An XOR linked list is a more memory efficient doubly linked list. 
# Instead of each node holding next and prev fields, it holds a field named both, 
# which is an XOR of the next node and the previous node. Implement an XOR linked list; 
# it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

# If using a language that has no pointers (such as Python), 
# you can assume you have access to get_pointer and dereference_pointer
# functions that converts between nodes and memory addresses.

# --------------------------------------------------------------------------

# This gets RIGHTEOUSLY confusing as fuck -- and I have no way to test it since
# it won't actually compile -- but I'm 85% certain the core logic is sound

def get_ptr(node):
	# returns a pointer to the provided node
def deref_ptr(pointer):
	# returns the node object to which pointer points

class XOR_Node(object):
	# The constructor for an XOR_Node object - args are a value for the node
	# and a pointer to another node in the list (usually, but not always, the previous node)
	def __init__(self, value=None, addr=0):
		self.val = value
		self.both = addr

class XOR_DLL(object):
	# No defaults here - user must provide a value for the head Node
	def __init__(self, value):
		# Our initial set-up consists of a head node, with val = value and both = *tail,
		# and a tail node, with val = None and both = *head
		self.head = XOR_Node(value, get_ptr(XOR_Node()))
		self.tail = deref_ptr(self.head.both)
		self.tail.both = get_ptr(self.head)

	def add(self, element):
		# store the new element in the previously valueless tail node
		self.tail.val = element
		# create a new tail node who's 'both' field is a ptr to the old tail
		self.tail = XOR_Node(value=None, get_ptr(self.tail))
		# update the 'both' field of the old tail by XORing with a ptr to the new tail
		deref_ptr(self.tail.both).both ^= get_ptr(self.tail)

	def get(self, index): 
		back_node = self.head
		# Recall that the 'both' field of head simply points to the second node
		fwd_node = deref_ptr(self.head.both)
		curr_idx = 0
		while(curr_idx < index):
			# Python is sexy and lets me do this in-place 
			back_node, fwd_node = fwd_node, deref_ptr(fwd_node.both ^ get_ptr(back_node))
			idx += 1
		return back_node.val





