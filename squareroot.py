'''
Hi, here's your problem today. This problem was recently asked by Google:

Given a positive integer, find the square root of the integer without using any built in square root \
    or power functions (math.sqrt or the ** operator). 
Give accuracy up to 3 decimal points.

'''
import sys
sys.setrecursionlimit(1500)

# Square root helper function using Binary Search
def sqrt_func_helper(n, p, q):
    mid = (p + q) / 2
    multiply = mid * mid

    if multiply == n:
        return mid

    elif multiply < n:
        return sqrt_func_helper(n, mid, q)

    else:
        return sqrt_func_helper(n, p, mid)


def sqrt(x):
    d = 1
    found = False # bool check sqrt while iterate
    while (found == False):
        if d*d == x:
            result = d
            found = True
        else:
            result = sqrt_func_helper(x, d-1, d)
            found = True
        d += 1
    return result



print(sqrt(5))
# 2.236
