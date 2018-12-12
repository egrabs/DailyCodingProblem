// Let's represent an integer in a linked list format by having each node represent a digit in the number. The nodes make up the number in reversed order.

// For example, the following linked list:

// 1 -> 2 -> 3 -> 4 -> 5
// is the number 54321.

// Given two linked lists in this format, return their sum in the same linked list format.

// For example, given

// 9 -> 9
// 5 -> 2
// return 124 (99 + 25) as:

// 4 -> 2 -> 1

function sumLLNums(n1, n2) {
    let carry = 0;
    let prev = null;
    let head = null;
    while (n1 || n2) {
        digit1 = n1 ? n1.val : 0;
        digit2 = n2 ? n2.val : 0;
        let newVal = digit1 + digit2 + carry;
        carry = newVal >= 10 ? 1 : 0;
        newVal = newVal % 10;
        const newNode = { val: newVal, next: null };
        if (head === null) head = newNode;
        if (prev) prev.next = newNode;
        prev = newNode;
        if (n1) n1 = n1.next;
        if (n2) n2 = n2.next;
        if (!n1 && !n2 && carry === 1) {
            const lastDigit = { val: 1, next: null };
            newNode.next = lastDigit;
        }
    }
    return head;
}

function printNumInLL(node) {
    stack = [];
    while (node) {
        stack.push(node.val);
        node = node.next;
    }
    stack.reverse();
    console.log( stack.join('') );
}

let a2 = { val: 9, next: null };
let a1 = { val: 9, next: a2 };

let b2 = { val: 2, next: null };
let b1 = { val: 5, next: b2 };
printNumInLL(sumLLNums(a1, b1));

let c5 = { val: 5, next: null };
let c4 = { val: 4, next: c5 };
let c3 = { val: 3, next: c4 };
let c2 = { val: 2, next: c3 };
let c1 = { val: 1, next: c2 };

let d1 = { val: 1, next: null };

printNumInLL(sumLLNums(c1, d1));
printNumInLL(sumLLNums(d1, c1));



