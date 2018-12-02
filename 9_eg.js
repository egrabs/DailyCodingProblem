"use strict";

// Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

// For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

// Follow-up: Can you do this in O(N) time and constant space?

function largestSumNonAdjacent(nums) {
    const sums = [];
    function subRoutine(nums, sum) {
        if (nums.length == 0) {
            sums.push(sum);
        } else {
            subRoutine(nums.slice(2), sum+nums[0]);
            subRoutine(nums.slice(1), sum);
        }
    }
    subRoutine(nums, 0);
    return Math.max(...sums);
}

console.log(largestSumNonAdjacent([2, 4, 6, 2, 5]));

console.log(largestSumNonAdjacent([5, 1, 1, 5]));