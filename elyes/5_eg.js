// cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
// For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

// Given this implementation of cons:

// def cons(a, b):
//     def pair(f):
//         return f(a, b)
//     return pair
// Implement car and cdr.

// python? nah this one gon be js

function cons(a, b) {
    function pair(f) {
        return f(a, b);
    }
    return pair;
}

function car(pair) {
    function getFirst(a, b) {
        return a;
    }
    return pair(getFirst);
}

function cdr(pair) {
    function getLast(a, b) {
        return b;
    }
    return pair(getLast);
}

console.log(car(cons(3, 4)) === 3);
console.log(car(cons(3,4)) === 4);