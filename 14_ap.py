# The area of a circle is defined as pir^2. Estimate pi to 3 decimal places 
# using a Monte Carlo method.

# Hint: The basic equation of a circle is x^2 + y^2 = r^2.

import random as rand

def estimate_pi(N):
    points = []
    r = 0.5
    in_circ = 0.0
    for i in range(N+1):
        points.append((rand.uniform(-r,r), rand.uniform(-r,r)))

    for p in points:
        if (p[0]**2 + p[1]**2) <= r**2:
            in_circ += 1
    
    pi = 4*(in_circ/N)
    return pi

print(estimate_pi(1000000))


