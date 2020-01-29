'''
Hi, here's your problem today. This problem was recently asked by Microsoft:

Given a list of numbers, and a target number n, \
    find all unique combinations of a, b, c, d, such that a + b + c + d = n.

Here's some examples and some starting code.
'''
def fourSum(nums, target):
    nums.sort()
    data = []
    length = len(nums)
    for i in range(length):
        for j in range(i,length):
            for k in range(j,length):
                for l in range(k,length):
                    boolean = (i!=j and i!=k and i!=l and j!=k and j!=l and k!=l)
                    if nums[i]+nums[j]+nums[k]+nums[l] == target and boolean:
                        data.append([nums[i], nums[j], nums[k], nums[l]])


    result = []
    for iterate in data:
        if iterate not in result:
            result.append(iterate)
    return result




print(fourSum([1, 1, -1, 0, -2, 1, -1], 0))
# print [[-1, -1, 1, 1], [-2, 0, 1, 1]]

print(fourSum([3, 0, 1, -5, 4, 0, -1], 1))
# print [[-5, -1, 3, 4]]

print(fourSum([0, 0, 0, 0, 0], 0))
# print ([0, 0, 0, 0])
