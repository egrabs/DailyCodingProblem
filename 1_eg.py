# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?


def twoNumsSumToKNaive(nums, k):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == k:
                return True
    return False


def twoNumsSumToK(nums, k):
    numMap = {}
    for num in nums:
        if num in numMap:
            return True
        else:
            # mark the remainder
            numMap[k-num] = 0
    return False

print twoNumsSumToKNaive([10, 15, 3, 7], 17)

print twoNumsSumToK([10, 15, 3, 7], 17)

print twoNumsSumToKNaive([10, 15, 3, 9, 17], 17)

print twoNumsSumToK([10, 15, 3, 9, 17], 17)