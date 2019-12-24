'''
Hi, here's your problem today. This problem was recently asked by AirBNB:

The power function calculates x raised to the nth power. 
If implemented in O(n) it would simply be a for loop over n and multiply x n times. 
Instead implement this power function in O(log n) time. You can assume that n will be a non-negative integer.
'''


def pow(x, n):
    if n == 0:
        return 1
    
    tempx = pow(x, int(n/2))
    GENAP = n % 2 == 0
    
    if GENAP:
        return tempx*tempx

    else:
        return x*tempx*tempx


print(pow(5, 3))
# 125
