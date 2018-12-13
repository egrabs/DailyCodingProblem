# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers
# in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1],
# the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

from functools import reduce

def productNotYou(nums):
    prod_nums = reduce(lambda x,y: x*y, nums)
    new_nums = [prod_nums/x for x in nums]
    print new_nums

def productNoGoogle(nums):
    prod_nums = 1
    for i in nums:
        prod_nums = prod_nums*i
    new_nums = [prod_nums/x for x in nums]
    print new_nums

def productNoDiv(nums):
    num_inds = range(0,len(nums))
    new_nums=[1]*len(nums)
    for i in num_inds:
        for k in num_inds:
           if k!=i: 
                new_nums[i]=new_nums[i]*nums[k]
    print new_nums

productNotYou([1, 2, 3, 4, 5])
productNoGoogle([1, 2, 3, 4, 5])
productNoDiv([1, 2, 3, 4, 5])
