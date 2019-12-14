'''
Hi, here's your problem today. This problem was recently asked by Facebook:

Given an array and an integer k, rotate the array by k spaces. 
Do this without generating a new array and without using extra space.

'''
def rotate_list(nums, k):
    n = len(nums)
    nums[:] = nums[::-1] # balikin semua list
    nums[0:k] = nums[0:k][::-1] # balikin dari 0-k lalu assign nilai baru
    nums[k:n] = nums[k:n][::-1] # balikin dari k-n lalu assign nilai baru sisa
    return nums

a = [1, 2, 3, 4, 5]
rotate_list(a, 3)
print(a)
# [3, 4, 5, 1, 2]
