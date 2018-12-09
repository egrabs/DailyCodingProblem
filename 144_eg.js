// Given an array of numbers and an index i, return the index of the nearest larger number
// of the number at index i, where distance is measured in array indices.

// For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.

// If two distances to larger numbers are the equal, then return any one of them.
// If the array at i doesn't have a nearest larger integer, then return null.

function nearestLarger(arr, i) {
    let after = i,
        before = i;
    while (after < arr.length || before > 0) {
        if (after < arr.length)
            after++;
        if (before > 0)
            before--;
        if (arr[after] > arr[i])
            return after;
        if (arr[before] > arr[i])
            return before;
    }
    return null;
}

console.log(nearestLarger([4, 1, 3, 5, 6], 0) === 3);