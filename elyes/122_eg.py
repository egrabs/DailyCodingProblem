# You are given a 2-d matrix where each cell represents number of coins in that cell. Assuming we start at matrix[0][0],
# and can only move right or down, find the maximum number of coins you can collect by the bottom right corner.

# For example, in this matrix

# 0 3 1 1
# 2 0 0 4
# 1 5 3 1
# The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.

def maxCoins(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i == 0 and j == 0:
                pass
            elif i == 0:
                mat[i][j] += mat[i][j-1]
            elif j == 0:
                mat[i][j] += mat[i-1][j]
            else:
                mat[i][j] += max(mat[i-1][j], mat[i][j-1])
    return mat[-1][-1]

tst = [[0,3,1,1], [2,0,0,4], [1,5,3,1]]

print(maxCoins(tst) == 12)