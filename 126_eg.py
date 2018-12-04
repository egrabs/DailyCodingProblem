# Write a function that rotates a list by k elements. For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2].
# Try solving this without creating a copy of the list. How many swap or move operations do you need?

def rotateNaive(arr, k):
    # an actual or "effective" k
    kAct = k % len(arr)
    if kAct == 0:
        return arr
    newArr = [None]*len(arr)
    for i in range(kAct):
        newArr[len(arr) - k + i] = arr[i]
    for i in range(kAct, len(arr)):
        newArr[i - kAct] = arr[i]
    return newArr

print 'make a new array'

print rotateNaive([1, 2, 3, 4, 5, 6], 1)
print rotateNaive([1, 2, 3, 4, 5, 6], 2)
print rotateNaive([1, 2, 3, 4, 5, 6], 3)
print rotateNaive([1, 2, 3, 4, 5, 6], 4)
print rotateNaive([1, 2, 3, 4, 5, 6], 5)
print rotateNaive([1, 2, 3, 4, 5, 6], 6)

print '\n\n\n'


def rotate(arr, k):
    # rotate by 1 k times
    for _ in range(k):
        # rotate by 1
        for i in range(len(arr) - 1):
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
    return arr

print 'in place'

print rotate([1, 2, 3, 4, 5, 6], 1)
print rotate([1, 2, 3, 4, 5, 6], 2)
print rotate([1, 2, 3, 4, 5, 6], 3)
print rotate([1, 2, 3, 4, 5, 6], 4)
print rotate([1, 2, 3, 4, 5, 6], 5)
print rotate([1, 2, 3, 4, 5, 6], 6)