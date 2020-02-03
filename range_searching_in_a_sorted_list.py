#!/usr/bin/python3

'''
Hi, here's your problem today. This problem was recently asked by Twitter:

Given a sorted list with duplicates, and a target number n, \
    find the range in which the number exists (represented as a tuple (low, high), both inclusive. 
    If the number does not exist in the list, return (-1, -1)).

Here's some examples and some starter code.
'''

def find_num(nums, target):
    nums.sort()
    start = 0
    end = len(nums)

    if target not in nums:
        return (-1,-1)
    
    for i in range(len(nums)):
        if target == nums[i]:
            start = i
            break
        else:
            continue

    # Last and only one number in that range
    if start == len(nums)-1:
        return (start,start)

    
    # All the remainder numbers
    last = 0
    for jj in range(start,end):
        if nums[jj] == target:
            last = jj
    return (start,last)

print(find_num([1, 1, 3, 4, 1], 4))
# (0, 1)
print(find_num([1, 2, 3, 4], 5))
# (-1, -1)