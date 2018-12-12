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
    # "mutable" string for the purposes of this question
    string = ctypes.create_string_buffer(s)
    start = 0
    end = 0
    while end < len(string):
        if end == len(string)-1 or string[end] == ' ':
            # reverse each word
            reverse(string, start, end-1)
            start = end+1
        end += 1
    # reverse the whole string after the words have been reversed
    reverse(string, 0, len(string)-2)
    return string.value

def reverse(string, start, end):
    while start < end:
        tmp = string[start]
        string[start] = string[end]
        string[end] = tmp
        start += 1
        end -= 1

print(reverseWords('hello world here is a string that should be reversed in place'))
