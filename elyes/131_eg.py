# Given the head to a singly linked list, where each node also has a "random" pointer that points to anywhere
# in the linked list, deep clone the list.

import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.rand = None

    def __str__(self):
        return 'val: {}, next: {}, rand: {}'.format(self.val, self.next.val if self.next else 'null', self.rand.val)

def deepClone(head):
    old = head
    while old != None:
        new = Node(old.val)
        new.next = old.next
        temp = old.next
        old.next = new
        old = temp
    old = head
    while old != None:
        # each old node points to it's new node muhahahaah
        old.next.rand = old.rand.next
        old = old.next.next
    new = newHead = head.next
    while new.next != None:
        new.next = new.next.next
        new = new.next
    return newHead

# Test

e = Node(5)
d = Node(4)
d.next = e
c = Node(3)
c.next = d
b = Node(2)
b.next = c
a = Node(1)
a.next = b

d.rand = e
a.rand = e
e.rand = c
c.rand = a
b.rand = d

aa = a
while aa:
    print str(aa)
    aa = aa.next

print '\n\n'

newA = deepClone(a)
while newA:
    print str(newA)
    newA = newA.next
