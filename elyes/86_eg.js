// Given a string of parentheses,
// write a function to compute the minimum number of parentheses to be removed to make the string valid (i.e. each open parenthesis is eventually closed).

// For example, given the string "()())()", you should return 1. Given the string ")(", you should return 2, since we must remove all of them.

function deletionsToBalanceParens(str) {
    parenStack = [];
    deletions = 0;
    for (let char of str) {
        if (char === '(')
            parenStack.push(char);
        else if (char === ')') {
            if (parenStack.length === 0)
                deletions++;
            else
                parenStack.pop();
        }
    }
    deletions += parenStack.length;
    return deletions;
}

console.log(deletionsToBalanceParens('()())()') === 1);
console.log(deletionsToBalanceParens(')(') === 2);
