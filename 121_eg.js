// Given a string which we can delete at most k, return whether you can make a palindrome.

// For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'.

// dood
// dfd
// 

function canMakePalindrome(str, k) {
    function isPalindrome(str, deletions) {
        if (deletions > k) {
            return false;
        }
        let j = str.length - 1;
        let i = 0;
        while (i <= j) {
            if (str[i] !== str[j]) {
                return isPalindrome(str.slice(0, i) + str.slice(i+1), deletions+1) || isPalindrome(str.slice(0, j)+str.slice(j+1), deletions+1);
            }
            i++;
            j--;
        }
        return true;
    }
    return isPalindrome(str, 0);
}

console.log(canMakePalindrome('waterrfetawx', 2));
console.log(canMakePalindrome('waterrfetawx', 1));
console.log(canMakePalindrome('waterretaw', 0));
console.log(canMakePalindrome('waterretaw', 2));
