# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not allowed.

class Stack(object):
	"""A simple Stack class"""
	def __init__(self):
			self.values = []

	def push(self, val):
		self.values.append(val)

	def pop(self):
		if len(self.values) > 0:
			return self.values.pop(len(self.values)-1)
		# else return None is implied

	def peek(self):
		if len(self.values) > 0:
			return self.values[len(self.values)-1]
		# else return None is implied

	def is_empty(self):
		return (len(self.values) == 0)

	def contents(self):
		for val in self.values:
			print(val)


# Create a mapping of ints 1..26 to chars a..z
chars = 'abcdefghijklmnopqrstuvwxyz'
character_map = dict()
for i in range(1,27):
	character_map[i] = chars[i-1]

# Preconditions/Assumptions - each msg has at least 1 encoding: 
# ie an empty string is not a valid message and will break the algorithm
def decode_count(char_map, msg):
	s = Stack()
	cnt, idx = 0, 0
	just_popped = False
	
	while(True):
		# If the currently observed state is an acceptable final state,
		# iterate cnt and see if there are any stacked previous states to return to,
		# else the task is complete and we return the cnt of possible encodings
		if idx == len(msg)-1:
			cnt += 1
			if s.is_empty(): 
				return cnt
			else:
				 idx = s.pop()
				 just_popped = True
				 continue

		if just_popped:
			just_popped = False
		elif (idx+1 < len(msg)) and (int(msg[idx:idx+2]) in char_map.keys()):
			# if the character encoded by ith and i+1th indexes is valid, push i+1th index.
			# this represents a new "branch" so to speak of parsing paths
			s.push(idx+1)

		idx += 1

# Only god knows this algorithm's complexity :(

print('Expected 3 ---> {}'.format(decode_count(character_map, '111')))
print('Expected 5 ---> {}'.format(decode_count(character_map, '1111')))
print('Expected 1 ---> {}'.format(decode_count(character_map, '293')))



