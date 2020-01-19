'''
Hi, here's your problem today. This problem was recently asked by Google:

Given a list of numbers and a target number n, find 3 numbers in the list that sums closest to the target number n.
 There may be multiple ways of creating the sum closest to the target number, you can return any combination in any order.

Here's an example and some starter code.
'''

import sys


def closest_3sum(nums, target):
    error = sys.maxsize  # big number
    nums.sort()  # sort the list of numbers
    length_lst = len(nums)
    get_numbers = []
    # print(nums)

    # loop remainder numbers in list
    for i in range(0, length_lst - 2):
        begin = i+1
        end = length_lst - 1
        while begin < end:

            if abs(nums[i] + nums[begin] + nums[end] - target) < error:
                error = abs(nums[i] + nums[begin] + nums[end] - target)
                print("Loops {}: {}".format(i,error))
                # solution = nums[i] + nums[begin]+ nums[end]
                get_numbers.append(nums[i])
                get_numbers.append(nums[begin])
                get_numbers.append(nums[end])

            if nums[i] + nums[begin]+ nums[end] > target:
                end -= 1
            else:
                begin += 1

    return get_numbers


print(closest_3sum([2, 1, -5, 4], -1))
# Closest sum is -5+1+2 = -2 OR -5+1+4 = 0
# print [-5, 1, 2]
