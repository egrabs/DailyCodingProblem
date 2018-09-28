# Implement an autocomplete system. That is, given a query string s 
# and a set of all possible query strings, return all strings in the 
# set that have s as a prefix.

# For example, given the query string 'de' and the 
# set of strings ['dog', 'deer', 'deal'], return [deer, deal].

# Hint: Try preprocessing the dictionary into a more efficient 
# data structure to speed up queries

from time import sleep

# Implement a 26-nary tree structure for preprocessing 
class Alpha_Node:
    def __init__(self, val={}):
        self.val = val
        # We'll use a dictionary where char keys map to Alpha_Node objects 
        self.links = dict()

class Prefix_Parser:
	def __init__(self, words):
		self.root = Alpha_Node(words)
		self.populate_parser(self.root, 0)

	def populate_parser(self, node, s_idx):

		for char in 'abcdefghijklmnopqrstuvwrxyz':
			word_group = set(filter(
							lambda s: (len(s) > s_idx) and s[s_idx] == char, 
							node.val))
			if word_group == set(): continue
			
			node.links[char] = Alpha_Node(word_group)
			self.populate_parser(node.links[char], s_idx+1)

	def search_prefix(self, prefix):
		sub_tree_root = self.root
		for char in prefix:
			if char not in sub_tree_root.links.keys(): return None
			sub_tree_root = sub_tree_root.links[char]
		return list(sub_tree_root.val) # Everyone likes lists, right?


# --------- Testing --------------
parser = Prefix_Parser(possibilities)
possibilities = {'dog', 'deer', 'deal', 'love', 'darn'}
test_s1, test_s2 = 'de','l'
print('Expected \'deer\',\'deal\' --> {}'.format(parser.search_prefix(test_s1)))
print('Expected \'love\' --> {}'.format(parser.search_prefix(test_s2)))


