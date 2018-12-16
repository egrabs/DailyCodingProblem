# Given a list of integers and a number K, return which contiguous elements of the list sum to K.

# For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4].

def whichSum(lst, k):
    s = sum(lst)
    slc = None
    def recurse(lst, s):
        nonlocal slc
        if len(lst) == 0:
            return
        if s == k:
            slc = lst
        else:
            recurse(lst[0: len(lst)-1], s-lst[-1])
            recurse(lst[1:], s-lst[0])
    recurse(lst, s)
    return slc

# hmm this returns [4,5] instead of [2,3,4] . . . but I mean . . . it's not wrong . . .
print(whichSum([1, 2, 3, 4, 5], 9))