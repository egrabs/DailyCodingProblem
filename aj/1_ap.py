# Daily Problem #1

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

def twoSum(nums, k):
        hashee = {}
        for idx in range(len(nums)):
            num = nums[idx]
            diff = k - num
            check = hashee.get(diff, -1)
            if check != -1:
                return True
            hashee[num] = idx
        return False
    
# Time and Space complexity should both be O(n)

print("\nShould be True: ", twoSum([1,2,4,0,10], 11))
print("\nShould be False: ", twoSum([1,2,4,0,3], 11))


