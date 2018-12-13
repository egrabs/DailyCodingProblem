// Given a number in the form of a list of digits, return all possible permutations.

// For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].

function permute(nums) {
    const perms = [];
    function recurse(nums, perm) {
        if (nums.length === 0) {
            perms.push(perm);
        } else {
            for (let i=0; i<nums.length; i++) {
                recurse(nums.slice(0, i).concat(nums.slice(i+1)) , perm.concat([nums[i]]))
            }
        }
    }
    recurse(nums, []);
    return perms;
}

console.log(permute([1,2,3]));
