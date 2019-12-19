'''
Hi, here's your problem today. This problem was recently asked by Apple:

Given a list of words in a string, reverse the words in-place (ie don't create a new string and reverse the words). 
Since python strings are not mutable, you can assume the input will be a mutable sequence (like list).
'''

def reverse_words(words):
    global s
    m = ''.join(words).split()[::-1]
    s = ['{} '.format(kata) for kata in m]
    return s

s = list("can you read this")
reverse_words(s)
print(''.join(s))
# this read you can
