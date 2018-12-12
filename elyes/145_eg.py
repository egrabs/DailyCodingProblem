# Given the head of a singly linked list, swap every two nodes and return its head.

# For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.

def swapTwo(head):
    curr = head
    while curr:
        if curr.next:
            tmp = curr.val
            curr.val = curr.next.val
            curr.next.val = tmp
            curr = curr.next.next
        else:
            curr = None

    return head

def swapTwoRecursive(head, prev):
    curr = head
    if curr:
        if curr.next:
            newHead = curr.next.next
            tmp = curr
            curr = curr.next
            curr.next = tmp
            swapTwoRecursive(newHead, tmp)
        if prev:
            prev.next = curr
    return curr

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def printMuhList(head):
    s = ''
    while head:
        s += str(head.val)
        s += '->'
        head = head.next
    s += 'null'
    print(s)

def makeLL():
    five = Node(5)
    four = Node(4, five)
    three = Node(3, four)
    two = Node(2, three)
    one = Node(1, two)
    return one

printMuhList(makeLL())

printMuhList(swapTwo(makeLL()))

printMuhList(swapTwoRecursive(makeLL(), None))
