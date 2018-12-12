"use strict";

// Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

// For example, given the following matrix:

// [[1,  2,  3,  4,  5],
//  [6,  7,  8,  9,  10],
//  [11, 12, 13, 14, 15],
//  [16, 17, 18, 19, 20],
//  [21, 22, 23, 24, 25]]

// You should print out the following:

// 1
// 2
// 3
// 4
// 5
// 10
// 15
// 20
// 19
// 18
// 17
// 16
// 11
// 6
// 7
// 8
// 9
// 14
// 13
// 12


const EX = [[1,  2,  3,  4,  5],
[6,  7,  8,  9,  10],
[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20]];

const EX2 = [[1,  2,  3,  4,  5],
[6,  7,  8,  9,  10],
[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20],
[21, 22, 23, 24, 25]];

function spiralOrder(matrix) {
    let n = matrix.length - 1,
        // assuming valid input because . . .it's a damn whiteboard problem
        m = matrix[0].length - 1,
        numElements = (n+1)*(m+1),
        horizBound = 0,
        vertBound = 0,
        i = 0,
        j = 0;

    const spiralOrdered = [];
    
    while (true) {
        if (j === horizBound && i === vertBound+1) {
            spiralOrdered.push(matrix[i][j]);
            i = ++vertBound;
            j = ++horizBound;
            m--;
            n--;
        }
        
        if (numElements === spiralOrdered.length) {
            return spiralOrdered;
        }

        spiralOrdered.push(matrix[i][j]);

        if (j < m && i === vertBound)
            j++;
        else if (j === m && i < n)
            i++;
        else if (i === n && j > horizBound)
            j--;
        else if (j === horizBound && i > vertBound+1)
            i--;
    }
}

console.log(EX);
spiralOrder(EX).forEach(n => console.log(n));

console.log('\n');

console.log(EX2);
spiralOrder(EX2).forEach(n => console.log(n));





