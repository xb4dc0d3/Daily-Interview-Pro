'''
Hi, here's your problem today. This problem was recently asked by LinkedIn:

You are only allowed to perform 2 operations, multiply a number by 2, or subtract a number by 1. 
Given a number x and a number y, find the minimum number of operations needed to go from x to y.

Here's an example and some starter code.
'''



def min_operations(x, y):

    # Base case
    if x == y:
        return 0
    if x > y:
        return x-y
    
    if y % 2 == 0 :
        return 1+min_operations(x,y//2)
    else:
        return 1+min_operations(x,y+1)


print(min_operations(6, 20))
# (((6 - 1) * 2) * 2) = 20 : 3 operations needed only
# print 3

# 20 / 2 = 10 sisa 0
# 10 / 2 = 5 sisa 0
# 5 / 2 = 2 sisa 1

# if sisa 1: x += 1 --> 6
# else sisa 0 : x

# 6 / 2 = 3 sisa 0

# (6+1+1)*2*2-1-1 = 30

# 31 / 2 = 15  sisa 1
# 32 / 2 = 16 sisa 0
# 16 / 2 = 8 sisa 0
# 8 / 2 = 4 sisa 0
# 4 / 2 = 2 sisa 0
