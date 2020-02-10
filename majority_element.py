'''
Hi, here's your problem today. This problem was recently asked by AirBNB:

A majority element is an element that appears more than half the time. 
Given a list with a majority element, find the majority element.

Here's an example and some starting code.
'''

def majority_element(nums):
    data = {}
    nums.sort()
    for i in nums:
        data[i] = data.get(i,0)+1
    
    max_values = max(data.values())
    return [key for key , values in data.items() if values == max_values][0]

print(majority_element([3, 5, 3, 3, 2, 4, 3]))
# 3
