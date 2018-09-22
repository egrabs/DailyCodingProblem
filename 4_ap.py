# Given an array of integers, find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. The array can 
# contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.

def first_missing_int(nums):
	low = 1
	for num in nums:
		if low == num:
			low += 1
	return low

print("Expected 3", first_missing_int([1,2,0]))
print("Expected 2", first_missing_int([3,4,-1,1]))
print("Expected 1", first_missing_int([-1,-2,0]))

# Linear time and constant space