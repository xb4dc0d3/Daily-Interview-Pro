'''
Hi, here's your problem today. This problem was recently asked by Apple:

Given a non-negative integer n, convert n to base 2 in string form. 
Do not use any built in base 2 conversion functions like bin.

'''


def base_2(n):
    res = ''
    
    while n != 0:
        if n % 2 == 0:
            res += '0'
        else:
            res += '1'
        n = n//2

    return res[::-1]


print(base_2(123))
# 1111011


# In the above example, 2^6 + 2^5 + 2^4 + 2^3 + 2^1 + 2^0 = 123.

# 123 / 2 = 61 rem 1
# 61 / 2 = 30 rem 1
# 30 / 2 = 15 rem 0
# 15 / 2 = 7 rem 1
# 7 / 2 = 3 rem 1
# 3 / 2 = 1 rem 1
# 1 / 2 = 0 rem 1
