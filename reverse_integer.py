'''
Hi, here's your problem today. This problem was recently asked by Amazon:

Given an integer, reverse the digits. Do not convert the integer into a string and reverse it.

Here's some examples and some starter code.
'''

def reverse_integer(num):
    rem = 0
    res = 0

    if "-" in str(num):
        len_num = len(str(num)[1:])
        num = int(str(num)[1:])

        while len_num!=0:
            rem = num % 10
            num = num // 10
            len_num -= 1
            res -= rem * int(str(1)+(str(0)*len_num))
            

    else:
        len_num = len(str(num))
        while len_num!=0:
            rem = num % 10
            num = num // 10
            len_num -= 1
            res += rem * int(str(1)+(str(0)*len_num))


    return res
  
print(reverse_integer(135))
# 531

print(reverse_integer(-321))
# -123


# 135 / 10 = 13 sisa 5
# 13 / 10 = 1 sisa 3
# 1 / 10 = 0 sisa 1

# -321 / 10 = -32 sisa 1
# -32 / 10 = -3 sisa 2
# -3 / 10 = 0 sisa -3
