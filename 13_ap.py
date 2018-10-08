# Given an integer k and a string s, find the length of the longest 
# substring that contains at most k distinct characters.

# For example, given s = "abcba" and k = 2, the longest substring 
# with k distinct characters is "bcb".


def distinct_substr_len(s, k):
    curr_len, best_len = 0, 0
    used_chars = dict()
    for idx in range(len(s)):
        if s[idx] in used_chars:
            used_chars[s[idx]] = idx
            curr_len += 1
        elif k == 0:
            old_idx = min(used_chars.values())
            curr_len = idx - old_idx
            del used_chars[s[old_idx]]
            used_chars[s[idx]] = idx
        else:
            used_chars[s[idx]] = idx
            k -= 1
            curr_len += 1
        if curr_len > best_len: best_len = curr_len
    return best_len

# Runs in O(n) time w.r.t len(s); O(k) space

print('Expected 3-->{}'.format(distinct_substr_len('abcba',2)))
print('Expected 4-->{}'.format(distinct_substr_len('aabccc',2)))
