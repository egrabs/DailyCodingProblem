# Given a list of integers, write a function that returns the largest sum 
# of non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. 
# [5, 1, 1, 5] should return 10, since we pick 5 and 5.

# Follow-up: Can you do this in O(N) time and constant space?

def non_adj_sum(nums):
	curr_sum, prev_sum = 0, 0
	idx_valid = True
	for num in nums:

		if num <= 0: 
			idx_valid = True
			continue
		if idx_valid:
			prev_sum = curr_sum
			curr_sum += num
			idx_valid = False
		elif prev_sum+num > curr_sum:
			curr_sum, prev_sum = prev_sum+num, curr_sum
			idx_valid = False
		else:
			prev_sum += num
			idx_valid = True

	return curr_sum

print('Expected 10 -> {}'.format(non_adj_sum([5,1,1,5])))
print('Expected 9 -> {}'.format(non_adj_sum([5,4,3,2,1])))
print('Expected 13 -> {}'.format(non_adj_sum([2,4,6,2,5])))

# O(n) time and O(1) space mothafuaaaaaa

