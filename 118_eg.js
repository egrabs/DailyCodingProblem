// Given a sorted list of integers, square the elements and give the output in sorted order
// eg: [-9, -2, 0, 2, 3] => [0, 4, 4, 9, 81]

const assert = require('assert');

function squareAndSort(sortedArr) {
    if (sortedArr.length < 2)
        return sortedArr.map(i => i*i);
    const squaredAndSorted = sortedArr.map(_ => null);
    let endex = sortedArr.length - 1;
    let startdex = 0;
    let added = 0;
    while (added < sortedArr.length) {
        const endIsGreater = Math.abs(sortedArr[endex]) > Math.abs(sortedArr[startdex]);
        const toSquare = endIsGreater ? sortedArr[endex] : sortedArr[startdex];
        squaredAndSorted[sortedArr.length - 1 - added] = toSquare*toSquare;
        if (endIsGreater) endex--;
        else startdex++;
        added++;
    }

    // sanity check
    assert(squaredAndSorted.every(i => i !== null))

    return squaredAndSorted;
}

console.log(squareAndSort([-9, -2, 0, 2, 3]));
