// You're given a string consisting solely of (, ), and *. * can represent either a (, ), or an empty string.
// Determine whether the parentheses are balanced.

// For example, (()* and (*) are balanced. )*( is not balanced.

function parensAreBalanced(s) {
    const stack = [];
    let freebies = 0;
    for (let char of s) {
        if (char === '(')
            stack.push(char);
        if (char === ')') {
            if (stack.length === 0)
                if (--freebies < 0)
                    return false;
            else
                stack.pop();
        }
        if (char === '*')
            freebies++;
    }
    return stack.length === 0 || freebies >= 0;
}

console.log(parensAreBalanced('(()*') === true);
console.log(parensAreBalanced('(*)') === true);
console.log(parensAreBalanced(')*(') === false);
