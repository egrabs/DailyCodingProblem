# Given a function f, and N return a debounced f of N milliseconds.

# That is, as long as the debounced f continues to be invoked, f itself will not be called for N milliseconds.

from time import time


def debounce(f, N):
    N /= 1000. # convert to seconds instead of ms since that's what time() returns

    # intiially set to time - N to that the first call succeeds if it happens immediately

    # have to use a dict instead of directly storing the value in a variable
    # so that we deal with method calls in the inner function instead of variable reassignment
    # a nested function in python can only reassign a variable in one of its outer function scopes in python3
    # and even then only using the 'nonlocal' keyword . . . bleh

    lastInvokation = {'time': time() - N}
    def wrapper():
        if (time() - lastInvokation['time']) < N:
            # in this case should the function be called once N milliseconds has been reached?
            # or should we just return None as I've assumed here
            return None
        else:
            lastInvokation['time'] = time()
            return f()
    return wrapper

def printHello():
    print('hello!')

debounced = debounce(printHello, 1000)

while True:
    debounced()