# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".


def longestSubWithKDistinct(s, k):
    maxLen = -1
    charsSeen = {}
    start = 0
    for i in range(len(s)):
        if s[i] in charsSeen:
            charsSeen[s[i]] += 1
        else:
            if len(charsSeen) == k:
                maxLen = sum(charsSeen.values())
                while len(charsSeen) == k:
                    charsSeen[s[start]] -= 1
                    if charsSeen[s[start]] == 0:
                        del charsSeen[s[start]]
                    start += 1
            charsSeen[s[i]] = 1
    return max([maxLen, len(s) - start])



print longestSubWithKDistinct("abcba", 2)
print longestSubWithKDistinct("abcabcabcabcf", 3)