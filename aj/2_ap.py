# Daily Problem #2
# Given an array of integers, return a new array such that each element at index i of the new array 
# is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

def iProd(nums):
    tail_prod_dict, lead_prod_dict = {}, {}
    tail_product, lead_product = 1, 1
    output = []
        
    for idx in range(len(nums)):
        # store cummulative product of values up to idx from index 0
        tail_product *= nums[idx]
        tail_prod_dict[idx] = tail_product
    for idx in range(len(nums)-1, -1, -1):
        # store cummulative product of values down to idx from index -1 (end)
        lead_product *= nums[idx]
        lead_prod_dict[idx] = lead_product
    # construct output array
    for idx in range(len(nums)):
        output.append(tail_prod_dict.get(idx-1,1) * lead_prod_dict.get(idx+1,1))
        
    return output

# Both Space and Time complexity of O(n)

print(iProd([1,2,3,4,5]))