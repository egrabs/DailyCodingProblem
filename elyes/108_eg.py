# Given two strings A and B, return whether or not A can be shifted some number of times to get B.

# For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.

def canShiftToMakeString(a, b):
    if (len(a) != len(b)):
        return False
    return b in '{}{}'.format(a,a)

print(canShiftToMakeString('abcde', 'cdeab') == True)
print(canShiftToMakeString('abc', 'acb') == False)