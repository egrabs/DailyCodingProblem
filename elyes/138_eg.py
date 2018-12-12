# Find the minimum number of coins required to make n cents.

# You can use standard American denominations, that is, 1cent, 5cent, 10cent, and 25cent.

# For example, given n = 16, return 3 since we can make it with a 10cent, a 5cent, and a 1cent.

from math import floor
def minCoins(cents):
    # start with the biggest
    numQuarters = floor(cents / 25.)
    cents = cents % 25
    numDimes = floor(cents / 10.)
    cents = cents % 10
    numNickels = floor(cents / 5.)
    numPennies = cents % 5
    return int(numPennies + numNickels + numDimes + numQuarters)

print minCoins(0) == 0
print minCoins(1) == 1
print minCoins(21) == 3
print minCoins(16) == 3
print minCoins(56) == 4