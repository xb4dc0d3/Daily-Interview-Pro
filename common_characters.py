'''
Hi, here's your problem today. This problem was recently asked by Apple:

Given a list of strings, find the list of characters that appear in all strings.

Here's an example and some starter code:
'''

def common_characters(strs):
    intersect_sets = set(strs[0])
    
    for words in strs:
        intersect_sets.intersection_update(words)
 
    return list(intersect_sets)
print(common_characters(['google', 'facebook', 'youtube']))
# ['e', 'o']
