# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

def do_the_thing(the_list, k):
    sum_list = [i+j for i in the_list for j in the_list if i>=j]
    if k in sum_list:
        return True
    return False


print do_the_thing([10, 15, 3, 7], 17)

print do_the_thing([10, 15, 3, 9, 17], 17)

print do_the_thing([10, 15, 3, 7],17)
