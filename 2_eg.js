"use strict";

// Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers 
// in the original array except the one at i.

// For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], 
// the expected output would be [2, 3, 6].

// Follow-up: what if you can't use division?


function productOfAllButSelf(nums) {
    var productOfAll = nums.reduce((a,b) => a*b);
    return nums.map(n => productOfAll / n);
}


function productOfAllButSelfNoDivision(nums) {
    // build up two arrays, one where arr[i] contains the product of all numbers in nums with index < i (left of i)
    // and one where arr[i] contains the product of all numbers in nums with index > i (right of i)
    // use this to then build the product excluding the number itself, because by multiplying the values
    // in these two arrays we can get the desired product
    var productsToLeft = [1];
    var productsToRight = [];
    productsToRight[nums.length - 1] = 1;

    for (let i=1; i<nums.length; i++) {
        productsToLeft[i] = productsToLeft[i-1]*nums[i-1];
    }
    for (let j=nums.length-2; j>=0; j--) {
        productsToRight[j] = productsToRight[j+1]*nums[j+1];
    }

    return nums.map((n, i) => productsToLeft[i]*productsToRight[i]);
}

console.log(productOfAllButSelf([1, 2, 3, 4, 5]));

console.log(productOfAllButSelf([3, 2, 1]));

console.log(productOfAllButSelfNoDivision([1, 2, 3, 4, 5]));

console.log(productOfAllButSelfNoDivision([3, 2, 1]));