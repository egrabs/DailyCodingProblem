# Given a string of words delimited by spaces, reverse the words in string.
# For example, given "hello world here", return "here world hello"

# Follow-up: given a mutable string representation, can you perform this operation in-place?

import ctypes

def reverseWordsNaive(s):
    words = s.split(' ')
    words.reverse()
    return ' '.join(words)

print(reverseWordsNaive('hello world here'))

def reverseWords(s):
    string = ctypes.create_string_buffer(s)
    i = 0
    i_prev = 0
    j = len(string) - 1
    j_prev = len(string) - 1
    stepping = True
    backing = True
    print string.value
    while i < j:
        if string[i] == ' ':
            stepping = False
        if string[j] == ' ':
            backing = False
        if not stepping and not backing:
            stepping = True
            backing = True
            endIsLonger = j_prev-j > i-i_prev
            if endIsLonger:
                diff = (j_prev-j) - (i-i_prev)
                tmp_word = string[i_prev:i]
                tmp_rest = string[i:i+diff]
                string[i_prev:i+diff-1] = string[j+1:j_prev]
                string[j+diff:j_prev] = tmp_word
                string[i+diff-1:j+diff] = tmp_rest + string[i+diff:j+1]
            else:
                diff = (i-i_prev) - (j_prev-j)
                tmp_word = string[j+1:j_prev]
                tmp_rest = string[j-diff:j+1]
                string[j-diff:j_prev] = string[i_prev:i]
                string[i_prev:i-diff-1] = tmp_word
                string[i-diff-1:j-diff] = string[i:j-diff] + tmp_rest
            j_prev = j
            i_prev = i
        if backing:
            j -= 1
        if stepping:
            i += 1
    return string.value

print(reverseWords('hello world hereeee'))
