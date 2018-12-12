// Given a pivot x, and a list lst, partition the list into three parts.

// The first part contains all elements in lst that are less than x
// The second part contains all elements in lst that are equal to x
// The third part contains all elements in lst that are larger than x
// Ordering within a part can be arbitrary.

// For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be [9, 3, 5, 10, 10, 12, 14].


// O(n)
function partitionList(lst, x) {
    let less = [],
        equal = [],
        more = [];
    lst.forEach(n => {
        if (n < x) less.push(n);
        if (n === x) equal.push(n);
        if (n > x) more.push(n);
    });

    // partitioned = new Array(lst.length);

    // for (let i=0; i < lst.length; i++) {
    //     if (i < less.length) partitioned[i] = less[i];
    //     else if (i < equal.length + less.length) partitioned[i] = equal[i - less.length];
    //     else if (i < more.length + less.length + equal.length) partitioned[i] = more[i - less.length - equal.length];
    // }

    // return partitioned;

    return less.concat(equal, more);
}

// Constant space
function partitionListConstSpace(lst, x) {
    let less = 0,
        equal = 0,
        more = 0;

    lst.forEach(n => {
        if (n < x) less++;
        if (n === x) equal++;
        if (n > x) more++;
    });

    function swap(i, j) {
        const tmp = lst[i];
        lst[i] = lst[j];
        lst[j] = tmp;
    }

    for (let i = 0; i < lst.length; i++) {
        for (let j = 0; j < lst.length; j++) {
            let first = lst[i];
            let second = lst[j];
            if (first > x && i < less+equal) {
                if (second <= x && (j >= (less+equal))) {
                    swap(i, j);
                }
            }
            if (first === x) {
                if (i < less) {
                    if (second < x && j >= equal) {
                        swap(i, j);
                    }
                }
                if (i >= less+equal) {
                    if (second > x && j < less+equal) {
                        swap(i, j);
                    }
                }
            }
            if (first < x && i >= less) {
                if (second >= x && j < less) {
                    swap(i, j);
                }
            }
        }
    }

    return lst;
}

console.log(partitionList([9, 12, 3, 5, 14, 10, 10], 10));
console.log(partitionListConstSpace([9, 12, 3, 5, 14, 10, 10], 10));
