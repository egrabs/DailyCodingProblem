# Given an iterator with methods next() and hasNext(), create a wrapper iterator,
# PeekableInterface, which also implements peek(). peek shows the next element that would be returned on next().

# Here is the interface:

# class PeekableInterface(object):
#     def __init__(self, iterator):
#         pass

#     def peek(self):
#         pass

#     def next(self):
#         pass

#     def hasNext(self):
#         pass

class Empty(Exception):
    pass

class PeekableInterface(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self.peeked = None

    def peek(self):
        if self.peeked != None:
            return self.peeked
        elif self.iterator.hasNext():
            nextEl = self.iterator.next()
            self.peeked.append(nextEl)
            return nextEl
        else:
            raise Empty()

    def next(self):
        if self.peeked != None:
            tmp = self.peeked
            self.peeked = None
            return tmp
        elif self.iterator.hasNext():
            return self.iterator.next()
        else:
            raise Empty()

    def hasNext(self):
        return self.peeked != None or self.iterator.hasNext()



