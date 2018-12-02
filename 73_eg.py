# Given the head of a singly linked list, reverse it in-place.

# 1 -> 2 -> 3 -> 4
# 4 -> 3 -> 2 -> 1

# I know there's builtin stacks in python
# and I know even python lists have a .pop() method
# but whatever, why not jusss do it
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if len(self.stack) == 0:
            raise Exception("Cannot pop from empty stack.")
        val = self.stack[-1]
        del self.stack[-1]
        return val

    def isEmpty(self):
        return len(self.stack) == 0

class Node:
    def __init__(self, val, nextNode=None):
        self.val = val
        self.next = nextNode

def printLL(head):
    vals = []
    node = head
    while node is not None:
        vals.append(str(node.val))
        node = node.next
    print '->'.join(vals)

def reverseLinkedListWithStack(head):
    stk = Stack()
    node = head
    while (node is not None):
        stk.push(node)
        node = node.next

    newHead = stk.pop()
    node = newHead
    while (not stk.isEmpty()):
        node.next = stk.pop()
        node = node.next

    node.next = None
    return newHead

def reverseLinkedListInPlace(head):
    prev = head
    node = head.next
    prev.next = None
    while node is not None:
        temp = node.next
        node.next = prev
        prev = node
        node = temp
    return prev

def buildLL():
    four = Node(4)
    three = Node(3, four)
    two = Node(2, three)
    one = Node(1, two)
    return one

printLL(reverseLinkedListWithStack(buildLL()))
printLL(reverseLinkedListInPlace(buildLL()))

