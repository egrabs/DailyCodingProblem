# Gray code is a binary code where each successive value differ in only one bit, as well as when wrapping around.
# Gray code is common in hardware so that we don't see temporary spurious values during transitions.

# Given a number of bits n, generate a possible gray code for it.

# For example, for n = 2, one gray code would be [00, 01, 11, 10]


def grayCode(n):
    if n < 1:
        return None
    codes = [0]
    # could do 2**n in python
    # but this is a language agnostic way of computing 2^n
    numCodes = (1 << n) - 1
    for i in range(numCodes):
        bitToModify = i % n
        num = codes[-1]
        num ^= 1 << bitToModify
        codes.append(num)
    return codes

def tst(n, codes):
    template = '{:0' + str(n) + 'b}'
    s = '['
    s += ', '.join(list(map(lambda code: template.format(code), codes)))
    s += ']'
    print s

tst(1, grayCode(1))
tst(2, grayCode(2))
tst(3, grayCode(3))
tst(4, grayCode(4))
tst(5, grayCode(5))
