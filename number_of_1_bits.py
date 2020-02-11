'''
Hi, here's your problem today. This problem was recently asked by Google:

Given an integer, find the number of 1 bits it has.

Here's an example and some starting code.
'''

def one_bits(num):
    count = 0
    rem = 0
    strr = ""
    while num != 0:
        rem = num % 2
        num = num//2
        if rem == 1:
            count+=1

    return count,strr



print(one_bits(23))
# 4
# 23 = 0b1011