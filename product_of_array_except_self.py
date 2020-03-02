'''
Hi, here's your problem today. (You've reached the end of the problems for now - in the meanwhile, 
here is a random question. And visit CoderPro for more practice!) This problem was recently asked by Amazon:

You are given an array of integers. Return an array of the same size where the element at each index is 
the product of all the elements in the original array except for the element at that index.

For example, an input of [1, 2, 3, 4, 5] should return [120, 60, 40, 30, 24].

You cannot use division in this problem.

Here's a start:
'''

def products(nums):
    product = 1
    result = []
    for i in nums:
        product *= i

    for i in range(len(nums)):
        result.append(product//nums[i])

    return result


print(products([1, 2, 3, 4, 5]))
# [120, 60, 40, 30, 24]