'''
Hi, here's your problem today. This problem was recently asked by Google:

Given a list of numbers, for each element find the next element that is larger than the current element. 
Return the answer as a list of indices. If there are no elements larger than the current element, then use -1 instead.

'''

def larger_number(nums):
    get_index = []
    NOT_FOUND = -1
    len_nums = len(nums)

    for i in range(len_nums):
        this_state = True
        k = i+1 # check number next to current element

        while this_state and i != len_nums-1:
            if nums[i] < nums[k]:
                get_index.append(k)
                this_state = False
    
            elif nums[i] > nums[k] and k == len_nums-1:
                get_index.append(NOT_FOUND)
                this_state = False
        
            else:
                k += 1
        k = 0

    get_index.append(-1) # add last element, last array doesn't have next larger element

    return get_index
            
# print [2, 2, 3, 4, -1, -1]
print(larger_number([3, 2, 5, 6, 9, 8]))