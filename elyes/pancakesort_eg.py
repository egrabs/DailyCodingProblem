# Given an an unsorted array, sort the given array. You are allowed to do only following operation on array.

# flip(arr, i): Reverse array from 0 to i 

def flip(arr, i):
    s = 0
    while s < i:
        tmp = arr[i]
        arr[i] = arr[s]
        arr[s] = tmp
        i -= 1
        s += 1

def pancakeSort(arr):
    end = len(arr) - 1
    while end > 1:
        currMax = -float('inf')
        flipIdx = -1
        for i in range(end+1):
            if arr[i] > currMax:
                currMax = arr[i]
                flipIdx = i
        flip(arr, flipIdx)
        flip(arr, end)
        end -= 1
    return arr


a = [3,5,1,2,4,7,6]
print(pancakeSort(a))