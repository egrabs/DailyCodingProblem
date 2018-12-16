// Given a string and a set of characters, return the shortest substring containing all the characters in the set.

// For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".

function shortestSubstring(str, charSet) {
    function covers(substr) {
        // trying to force myself to start using const in loops
        // but it feels so wrong
        for (const char of charSet) {
            if (!substr.includes(char))
                return false;
        }
        return true;
    }
    let start = 0;
    let end = str.length;
    let substr = str.slice(start, end);
    while (covers(substr)) {
        substr = str.slice(++start, end);
    }
    substr = str.slice(--start, end);
    while (covers(substr)) {
        substr = str.slice(start, --end);
    }
    end++;
    return str.slice(start, end);
}

console.log(shortestSubstring('figehaeci', new Set(['a', 'e', 'i'])));
console.log(shortestSubstring('figehaei', new Set(['a', 'e', 'i'])));
console.log(shortestSubstring('figehaeciffrtq', new Set(['a', 'e', 'i'])));
