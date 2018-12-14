// Given a word W and a string S, find all starting indices in S which are anagrams of W.

// For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.


// I really hate this implementation. . . it's so ugly
// it could probably be 1000x better. Maybe I'll revisit it one day
// but for now it works and I'm too lazy
function allAnagramIndices(s, w) {
    function setCount(m, char) {
        if (m.has(char))
            m.set(char, m.get(char)+1);
        else
            m.set(char, 1);
    }
    const anagramChars = new Map();
    for (let char of w) {
        setCount(anagramChars, char)
    }
    function isAnagram(slice) {
        const sliceChars = new Map();
        for (let char of slice) {
            if (!anagramChars.has(char))
                return false;
            else
                setCount(sliceChars, char)
        }
        let reval = true;
        sliceChars.forEach((val, key) => {
            if (val !== anagramChars.get(key))
                reval = false;
        });
        return reval;
    }
    const sliceLen = w.length;
    if (s.length < w.length) return [];
    const anagramIndices = [];
    let start = 0;
    let end = sliceLen;
    while (start <= s.length - sliceLen) {
        let slice = s.slice(start, end);
        if (isAnagram(slice, w))
            anagramIndices.push(start)
        start++;
        end++;
    }
    return anagramIndices;
}

console.log(allAnagramIndices('abxaba', 'ab'))
console.log(allAnagramIndices('abxabafdgcabhjubappbya', 'ab'))
