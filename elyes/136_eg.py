# Given an N by M matrix consisting only of 1's and 0's,
# find the largest rectangle containing only 1's and return its area.

# For example, given the following matrix:

# [[1, 0, 0, 0],
#  [1, 0, 1, 1],
#  [1, 0, 1, 1],
#  [0, 1, 0, 0]]

# Return 4.

def largestOnesArea(mat):
    if len(mat) == 0 or len(mat[0]) == 0:
        return 0
    def helper(rowSlice, colSlice):
        rowStart, rowEnd = rowSlice
        colStart, colEnd = colSlice
        if colEnd-colStart == 0 or rowEnd-rowStart == 0:
            return 0
        slc = [row[colStart: colEnd] for row in mat[rowStart: rowEnd]]
        allOnesRow = lambda row: all(map(lambda n: n==1, row))
        if all(map(lambda row: allOnesRow(row), slc)):
            return (rowEnd-rowStart)*(colEnd-colStart)
        else:
            return max(
                helper((rowStart+1, rowEnd), colSlice),
                helper((rowStart, rowEnd-1), colSlice),
                helper(rowSlice, (colStart+1, colEnd)),
                helper(rowSlice, (colStart, colEnd-1))
            )
    return helper((0, len(mat)), (0, len(mat[0])))


matrix = [
    [1, 0, 0, 0],
    [1, 0, 1, 1],
    [1, 0, 1, 1],
    [0, 1, 0, 0]
]

print(largestOnesArea(matrix))