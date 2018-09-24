# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first 
# and last element of that pair. For example, car(cons(3, 4)) returns 3, 
# and cdr(cons(3, 4)) returns 4.

#Given this implementation of cons:
# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair
# Implement car and cdr.


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


# returns the first element of the pair
def car(pair):
	return pair(lambda *args : args[0])

# returns the last element of the pair
def cdr(pair):
	return pair(lambda *args : args[1])


print(car(cons(3,4)) == 3)
print(cdr(cons(3,4)) == 4)