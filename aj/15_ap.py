# Given a stream of elements too large to store in memory, 
# pick a random element from the stream with uniform probability.

# Had to look this one up :\
# https://www.dailycodingproblem.com/blog/how-to-pick-a-random-element-from-an-infinite-stream/
import random

def pick(big_stream):
    random_element = None

    for i, e in enumerate(big_stream):
        if i == 0:
            random_element = e
        elif random.randint(1, i + 1) == 1:
            random_element = e
    return random_element