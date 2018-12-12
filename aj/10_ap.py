# Implement a job scheduler which takes in a function f 
# and an integer n, and calls f after n milliseconds.

from time import sleep

def sched(f, n):
	milliseconds = n/1000
	sleep(milliseconds)
	f()

def f():
	print("\tDone Sleeping")

print("Sleeping 1.5 seconds...\n")
sched(f, 1500)
print("Sleeping 5.0 seconds...\n")
sched(f, 5000)