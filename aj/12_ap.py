# There exists a staircase with N steps, and you can climb up either 1 or 2 
# steps at a time. Given N, write a function that returns the number of unique 
# ways you can climb the staircase. The order of the steps matters.

# For example, if N is 4, then there are 5 unique ways:

# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
# What if, instead of being able to climb 1 or 2 steps at a time, you could 
# climb any number from a set of positive integers X? For example, if
# X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

def stair_routes(N, X):
    return recurse(0, 0, N, X)
def recurse(step, num_routes, N, X):
    if step == N:
        return num_routes + 1
    for x in X:
        if(step + x <= N): 
            num_routes = recurse(step+x, num_routes, N, X)
    return num_routes

print('Expected 5 -> {}'.format(stair_routes(4, {1,2})))