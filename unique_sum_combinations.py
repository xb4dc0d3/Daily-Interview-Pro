'''
Hi, here's your problem today. This problem was recently asked by Twitter:

Given a list of numbers and a target number, find all possible unique subsets of the list of numbers that \
    sum up to the target number. 
    The numbers will all be positive numbers.

Here's an example and some starter code.
'''

import sys
sys.setrecursionlimit(10000)

def subs_temp_fn(nums, temp, target, result):

    nums.sort()
    total_sum = sum(temp)
    if total_sum > target:
        return False

    elif total_sum == target:
        result.append(temp)
        return True
    else:
        for i in range(len(nums)):
            subs_temp_fn(nums[i:], temp+[nums[i]],target, result)

def sum_combinations(nums, target):
    if not nums:
        return []
    
    result = []

    subs_temp_fn(nums,[],target,result)

    final_result = []
    for arr in result:
        if sum(arr) == target and arr not in final_result:
            final_result.append(arr)

    return [tuple(i) for i in final_result]

print(sum_combinations([10, 1, 2, 7, 6, 1, 5], 8))
# [(2, 6), (1, 1, 6), (1, 2, 5), (1, 7)]