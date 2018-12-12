// Given a 2D array, print it in spiral form. See the following examples.

// Input:
//         1    2   3   4
//         5    6   7   8
//         9   10  11  12
//         13  14  15  16
// Output: 
// 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 


// Input:
//         1   2   3   4  5   6
//         7   8   9  10  11  12
//         13  14  15 16  17  18
// Output: 
// 1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11


function spiralizeMatrix(mat) {
    let i = 0;
    let j = 0;
    let leftBound = 0;
    let topBound = 0;
    let numRows = mat.length - 1;
    let numCols = mat[0].length - 1;
    const spiral = [];
    while (spiral.length < mat.length*mat[0].length) {
        spiral.push(mat[i][j]);

        if (i === topBound && j < numCols) j++;
        else if (j === numCols && i < numRows) i++;
        else if (i === numRows && j > leftBound) j--;
        else if (j === leftBound && i > topBound) i--;

        if (j === leftBound && i === topBound+1) {
            spiral.push(mat[i][j])
            leftBound++;
            topBound++;
            numRows--;
            numCols--;
            j++;
        }
    }
    return spiral;
}

const test1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
];

const test1_spiral = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10];


const test2 = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
];

const test2_spiral = [1, 2, 3, 4, 5, 6, 12, 18, 17, 16, 15, 14, 13, 7, 8, 9, 10, 11];

function equal(arr1, arr2) {
    if (arr1.length !== arr2.length)
        return false;
    for (let i=0; i<arr1.length; i++) {
        if (arr1[i] !== arr2[i])
            return false;
    }
    return true;
}

console.log(equal(spiralizeMatrix(test1), test1_spiral));

console.log(equal(spiralizeMatrix(test2), test2_spiral));




