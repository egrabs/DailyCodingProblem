// Given the head to a singly linked list, where each node also has a “random” pointer that points to anywhere
// in the linked list, deep clone the list.

const assert = require('assert');

function deepClone(head) {
    const oldToNew = new Map();
    let n = head;
    let prev = null;
    while (n) {
        const newNode = { val: n.val };
        if (prev)
            prev.next = newNode;
        oldToNew.set(n, newNode);
        prev = newNode;
        n = n.next;
    }
    n = head;
    while (n) {
        const newNode = oldToNew.get(n);
        const newRand = oldToNew.get(n.rand);
        newNode.rand = newRand;
        n = n.next;
    }
    return oldToNew.get(head);
}

// tests

const e = { val: 5, next: null }
const d = { val: 4, next: e, rand: e }
const c = { val: 3, next: d }
const b = { val: 2, next: c }
const a = { val: 1, next: b, rand: e}

e.rand = c;
c.rand = a;
b.rand = d;

const newA = deepClone(a);

const isEqual = (a, b) => {
    const nextIsEqual = !a.next && !b.next ? true : a.next.val === b.next.val;
    return nextIsEqual && a.val === b.val && a.rand.val === b.rand.val;
}

let knowd = a;
let newKnowd = newA;
while (knowd && newKnowd) {
    assert(isEqual(knowd, newKnowd));
    assert(knowd !== newKnowd);
    knowd = knowd.next;
    newKnowd = newKnowd.next;
}

console.log('Passed!')
