'''
You run an e-commerce website and want to record the last N order ids in a 
log. Implement a data structure to accomplish this, with the following API:
    - record(order_id): adds the order_id to the log
    - get_last(i): gets the ith last element from the log. i is guaranteed to 
      be smaller than or equal to N.
    - You should be as efficient with time and space as possible.
'''

class CommerceLog:
    def __init__(self, N):
        self.N = N
        self.log = [None for id in range(N)]

    def record(self, order_id):
        self.log.insert(0, order_id)
        self.log.pop(self.N)

    def get_last(self, i):
        if i <= 0: raise IndexError 
        return self.log[i-1]



com = CommerceLog(10)
for i in range(12): com.record(i)
print(com.log)
print('log length is {}'.format(len(com.log)))
print('2nd last element is {}'.format(com.get_last(2)))



