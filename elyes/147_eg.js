// Given a list, sort it using only this method: reverse(lst, i, j), which reverses lst from i to j.

function reverse(lst, i, j) {
    while (i < j) {
        let tmp = lst[i];
        lst[i] = lst[j];
        lst[j] = tmp;
        i++;
        j--;
    }
}

function reverseSort(arr) {
    function minDexFrom(i) {
        let min = Infinity;
        let mindex = -1;
        for (let idx=i; i<arr.length; i++) {
            if (arr[i] < min) {
                min = arr[i];
                mindex = i;
            }
        }
        return mindex;
    }
    let start = 0;
    while (start < arr.length) {
        mindex = minDexFrom(start);
        reverse(arr, mindex, arr.length-1);
        reverse(arr, start, arr.length-1);
        start++;
    }
    return arr;
}

a = [3,5,1,2,4,7,6];
console.log(reverseSort(a));
