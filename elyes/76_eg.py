# You are given an N by M 2D matrix of lowercase letters.
# Determine the minimum number of columns that can be removed to ensure that each row is ordered from top to bottom lexicographically.
# That is, the letter at each column is lexicographically later as you go down each row. It does not matter whether each row 
# itself is ordered lexicographically.

# For example, given the following table:

# cba
# daf
# ghi
# This is not ordered because of the a in the center. We can remove the second column to make it ordered:

# ca
# df
# gi
# So your function should return 1, since we only needed to remove 1 column.

# As another example, given the following table:

# abcdef
# Your function should return 0, since the rows are already ordered (there's only one row).

# As another example, given the following table:

# zyx
# wvu
# tsr
# Your function should return 3, since we would need to remove all the columns to order it.

def lexicographicDeletions(matrix):
	N = len(matrix)  # num rows
	M = len(matrix[0])  # num cols (assuming not jagged)
	deletions = 0
	for col in range(M):
		prev = -1
		for row in range(N):
			lexIdx = ord(matrix[row][col])
			if lexIdx < prev:
				deletions += 1
				break
			prev = lexIdx
	return deletions

tst1 = [
	['c', 'b', 'a'],
	['d', 'a', 'f'],
	['g', 'h', 'i']
]

tst2 = [['a', 'b', 'c', 'd', 'e', 'f']]

tst3 = [
	['z', 'y', 'x'],
	['w', 'v', 'u'],
	['t', 's', 'r']
]

print(lexicographicDeletions(tst1) == 1)
print(lexicographicDeletions(tst2) == 0)
print(lexicographicDeletions(tst3) == 3)
