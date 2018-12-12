# Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

# For example, given the following matrix:

# [[1,  2,  3,  4,  5],
#  [6,  7,  8,  9,  10],
#  [11, 12, 13, 14, 15],
#  [16, 17, 18, 19, 20]]

# You should print out the following:

# 1
# 2
# 3
# 4
# 5
# 10
# 15
# 20
# 19
# 18
# 17
# 16
# 11
# 6
# 7
# 8
# 9
# 14
# 13
# 12

import numpy as np

test_mat = np.array([[1,  2,  3,  4,  5],
					[6,  7,  8,  9,  10], 
					[11, 12, 13, 14, 15], 
					[16, 17, 18, 19, 20]])
test_mat2 = np.array([[1,  2,  3,  4,  5],
					 [6,  7,  8,  9,  10],
					 [11, 12, 13, 14, 15],
					 [16, 17, 18, 19, 20],
					 [21, 22, 23, 24, 25]])

def spiral(matrix):
	n = len(matrix[:,0])-1
	m = len(matrix[0])-1
	x = 0
	while(True):
		if (x == n and x == m): 
			print(matrix[n,m])
			break
		elif (x > n or x > m): break
		for i in matrix[x, x:m]: print(i)
		for i in matrix[x:n, m]: print(i)
		for i in matrix[n, m:x:-1]: print(i)
		for i in matrix[n:x:-1, x]: print(i)
		x += 1
		n -= 1
		m -= 1

#spiral(test_mat)
spiral(test_mat2)

