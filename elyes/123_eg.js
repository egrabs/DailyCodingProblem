// Given a string, return whether it represents a number.

//     Here are the different kinds of numbers:

//     "10", a positive integer
//     "-10", a negative integer
//     "10.1", a positive real number
//     "-10.1", a negative real number
//     "1e5", a number in scientific notation

//     And here are examples of non-numbers:

//     "a"
//     "x 1"
//     "a -2"
//     "-"

function parseNum(numStr) {
    const numReg = /^(-?(?:\d+(?:\.\d*)?|\.\d+)(?:e\d+)?)$/;
    return numReg.test(numStr);
}

// true
console.log(parseNum('10'));
console.log(parseNum('-10'));
console.log(parseNum('10.1'));
console.log(parseNum('-10.1'));
console.log(parseNum('1e5'));
console.log(parseNum('1.'));
console.log(parseNum('.1'));

console.log('\n\n');

// false
console.log(parseNum('.'));
console.log(parseNum('a'));
console.log(parseNum('x 1'));
console.log(parseNum('a -2'));
console.log(parseNum('-'));
console.log(parseNum(''))



