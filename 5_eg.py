# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair
# Implement car and cdr.

# Ok . . .fine I'll do it in python too

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    # hehe
    return pair(lambda x,y: x)

# https://i.kym-cdn.com/entries/icons/facebook/000/016/151/tumblr_inline_n327sfUDU01r3x7o0.jpg
cdr = lambda pair: pair(lambda x,y: y)

print car(cons(3,4)) == 3

print cdr(cons(3,4)) == 4