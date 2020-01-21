'''
Hi, here's your problem today. This problem was recently asked by Facebook:

Given two binary numbers represented as strings, return the sum of the two binary numbers as a new binary represented as a string.
Do this without converting the whole binary string into an integer.

Here's an example and some starter code.
'''


def sum_binary(bin1, bin2):

    len_bin1, len_bin2 = len(bin1), len(bin2)
    diff_len = abs(len_bin1 - len_bin2)
    res = ""

    # check if the longest, then the shortest added with zero
    if len_bin1 > len_bin2:
        bin2 = "0"*diff_len + bin2
        ll = len_bin1

    elif len_bin1 < len_bin2:
        bin1 = "0"*diff_len + bin1
        ll = len_bin2

    carry = 0
    for i in reversed((range(ll))):
        if int(bin1[i]) + int(bin2[i]) + carry == 0:
            res = '0' + res
        elif int(bin1[i]) + int(bin2[i]) + carry == 1:
            res = '1' + res
            carry = 0
        elif int(bin1[i]) + int(bin2[i]) + carry == 2:
            res = '0' + res
            carry = 1
        else:
            res = '1' + res
            carry = 1
    if carry == 1:
        res = '1' + res
    
    return res


print(sum_binary("11101", "1011"))
# 101000
