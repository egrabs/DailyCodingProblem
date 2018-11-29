# You have 100 fair coins and you flip them all at the same time. Any that come up tails you set aside.
# The ones that come up heads you flip again. How many rounds do you expect to play before only one coin remains?

# Write a function that, given n, returns the number of rounds you'd expect to play until one coin remains.

from math import log
def howManyFlips(n):
    return log(n) / log(2)

def howManyFlipsNoLog(n):
    count = 0
    while n > 1:
        n = n >> 1
        count += 1
    return count

print howManyFlips(8)
print howManyFlipsNoLog(8)