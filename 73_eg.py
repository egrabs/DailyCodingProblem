# Given the head of a singly linked list, reverse it in-place.

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
    def __init__(self, val):
        self.val = val
        self.next = None

def reverseLinkedList(head):
    stk = new Stack()
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
