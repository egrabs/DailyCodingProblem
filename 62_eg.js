// There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

// For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

// Right, then down
// Down, then right
// Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.

function fac(n) {

    if (n < 0) {
        console.warn('invalid argument to factorial: ', n);
        return -1;
    }

    if (n===0 || n ===1) {
        return 1;
    } else {
        return n*fac(n-1);
    }
}

function x_choose_y(x, y) {
    return fac(x) / (fac(y)*fac(x-y));
}

function numWays(n, m) {
    return x_choose_y(m+n-2, n-1);
}