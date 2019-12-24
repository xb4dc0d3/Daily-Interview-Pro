'''
Hi, here's your problem today. This problem was recently asked by Facebook:

Given a number n, find the least number of squares needed to sum up to the number.
'''

import math

def square_sum(n):
    status_dec = n
    count = 0
    while status_dec != 0:
        x = math.floor(math.sqrt(n))
        print(x)
        if n - x*x == 0:
            status_dec = 0
            count += 1
        else:
            n = n - x*x  
            count += 1   
    return count

print(square_sum(5))
# Min sum is 3^2 + 2^2
# 2