'''
Hi, here's your problem today. This problem was recently asked by Google:

Given a list of positive numbers, find the largest possible set such that no elements are adjacent numbers of each other.

Here's some example and some starter code
'''

def maxNonAdjacentSum(nums):
  prev1, prev2, result = 0 , 0, 0
  # prev 1 means the previous before of the list

  for idx in range(len(nums)):
    if idx == 0:
      result = nums[0]

    elif idx == 1:
      result = max(nums[0],nums[1])

    else:
      result = max(prev1, nums[idx] + prev2)

    prev2 = prev1
    prev1 = result # temp result

  return result


    
    
    
  
print(maxNonAdjacentSum([3, 4, 1, 1]))
# 5
# max sum is 4 (index 1) + 1 (index 3)

print(maxNonAdjacentSum([2, 1, 2, 7, 3]))
# 9
# max sum is 2 (index 0) + 7 (index 3)
