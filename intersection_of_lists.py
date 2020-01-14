'''
Hi, here's your problem today. This problem was recently asked by Twitter:

Given 3 sorted lists, find the intersection of those 3 lists.

Here's an example and some starter code.
'''

def intersection(list1, list2, list3):
    result = set()
    sets1, sets2, sets3 = set(list1), set(list2), set(list3)
    result = sets1.intersection(sets2,sets3)

    return list(result)
  
print(intersection([1, 2, 3, 4], [2, 4, 6, 8], [3, 4, 5]))
# [4]