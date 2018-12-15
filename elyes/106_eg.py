# This problem was asked by Pinterest.

# Given an integer list where each number represents the number of hops you can make,
# determine whether you can reach to the last index starting at index 0.

# For example, [2, 0, 1, 0] returns true while [1, 1, 0, 1] returns false.


# I'm assuming that you "can make n hops" as in if you land on n, you can make n hops or n-1 hops or n-2 hops or . . . 1 hop
def canMakeItToEnd(lst):
    pos = 0
    hops = 0
    while pos < len(lst) - 1:
        hops += lst[pos]
        if hops == 0 and pos < (len(lst) - 1):
            return False
        pos += 1
        hops -= 1
    return True

print(canMakeItToEnd([2, 0, 1, 0]) == True)
print(canMakeItToEnd([1, 1, 0, 1]) == False)
print(canMakeItToEnd([5, 0, 0, 4, 0, 0, 0]) == True)
print(canMakeItToEnd([5, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0]) == False)
print(canMakeItToEnd([0, 10, 10]) == False)
print(canMakeItToEnd([]) == True)
print(canMakeItToEnd([1, 1, 2, 0, 1, 3, 0, 0, 1, 4, 0, 0, 0, 0]) == True)