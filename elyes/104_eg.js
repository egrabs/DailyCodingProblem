// Determine whether a doubly linked list is a palindrome. What if it’s singly linked?

// For example, 1 -> 4 -> 3 -> 4 -> 1 returns true while 1 -> 4 returns false.

function llNode(val, prev, next=null) {
    this.val = val;
    this.prev = prev;
    this.next = next;
}

function buildRandomll(isDouble) {
    const getPrev = prev => isDouble ? prev : null;
    let last = null;
    let head;
    for (let i=0; i<Math.ceil(Math.random()*20); i++) {
        const n = new llNode(Math.random(), getPrev(last));
        if (i===0)
            head = n;
        if (last)
            last.next = n;
        last = n;
    }
    return head;
}

function buildEx1(isDouble) {
    const getPrev = prev => isDouble ? prev : null;
    const one = new llNode(1, null);
    const two = new llNode(4, getPrev(one));
    one.next = two;
    const three = new llNode(3, getPrev(two));
    two.next = three;
    const four = new llNode(4, getPrev(three));
    three.next = four;
    const five = new llNode(1, getPrev(four));
    four.next = five;
    return one;
}


// doubly
function isPalindromeDll(node) {
    const queue = [];
    let last;
    while (true) {
        queue.push(node);
        node = node.next;
        if (node.next === null)
            break;
    }
    while (queue.length > 0) {
        const head = queue.shift();
        if (head.val !== node.val)
            return false;
        node = node.prev;
    }
    return true;
}

// singly
function isPalindromeSll(node) {
    const queue = [];
    const stack = [];

    while (node !== null) {
        queue.push(node);
        stack.push(node);
        node = node.next;
    }

    // this condition really could check *just* the queue length or *just* the stack length but whatever
    while (queue.length > 0 && stack.length > 0) {
        const back = stack.pop();
        const front = queue.shift();
        if (back.val !== front.val)
            return false;
    }

    return true;
}

console.log(isPalindromeDll(buildEx1(true)));
console.log(isPalindromeSll(buildEx1(false)));

console.log(isPalindromeDll(buildRandomll(true)));
console.log(isPalindromeSll(buildRandomll(false)));








