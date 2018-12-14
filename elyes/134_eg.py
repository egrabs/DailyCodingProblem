# You have a large array with most of the elements as zero.

# Use a more space-efficient data structure, SparseArray, that implements the same interface:

# init(arr, size): initialize with the original large array and size.
# set(i, val): updates index at i with val.
# get(i): gets the value at index i.

class SparseArray:
    def __init__(self, arr, size):
        self.nonZeros = {};
        self.minInd = 0
        self.maxInd = size
        # just gonna assume that anything at indices between len(arr) and size is a 0 rather than None
        # since the problem description doesn't specify
        for i in range(min(size, len(arr))):
            if arr[i] != 0:
                self.nonZeros[i] = arr[i]

    def set(self, i, val):
        if i > self.maxInd:
            raise ValueError('Index out of bounds!')
        if val != 0:
            self.nonZeros[i] = val

    def get(self, i):
        if i > self.maxInd:
            raise ValueError('Index out of bounds!')
        if i in self.nonZeros:
            return self.nonZeros[i]
        return 0



sparseArr = [0]*100 + [1,2,3,4] + [0]*253 + [4,19,12,34,29]
sparseArr2 = [1,2,3] + [0]*306 + [19, 12, 14] + [0]*500
sparseArr3 = [45,16,7] + [0]*500 + [15,22,3] + [0]*926 + [28, 14]

arr1 = SparseArray(sparseArr, 1000)
arr2 = SparseArray(sparseArr2, 3000)
arr3 = SparseArray(sparseArr3, 2500)

print(arr1.get(100) == 1)
print(arr1.get(80) == 0)
print(arr1.get(999) == 0)
arr1.set(65, 13)
print(arr1.get(65) == 13)

print(arr2.get(2) == 3)


print(arr3.get(503) == 15)
print(arr3.get(506) == 0)

