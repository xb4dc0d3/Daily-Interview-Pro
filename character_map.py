'''
Hi, here's your problem today. This problem was recently asked by Google:

Given two strings, find if there is a one-to-one mapping of characters between the two strings.

Example

Input: abc, def
Output: True # a -> d, b -> e, c -> f

Input: aab, def
Ouput: False # a can't map to d and e 

Here's some starter code:
'''

def has_character_map(str1, str2):
    split_str1 = list(str1)
    split_str2 = list(str2)

    lst_to_set1 = set(split_str1)
    lst_to_set2 = set(split_str2)

    merge_set = dict(zip(lst_to_set1,lst_to_set2))

    return True if len(merge_set) >= max(len(split_str1), len(split_str2)) else False

print(has_character_map('abc', 'def'))
# True
print(has_character_map('aac', 'def'))
# False

print(has_character_map('abc', 'aabc'))
# False

print(has_character_map('bcda', 'abcd'))
#True

print(has_character_map("a","a"))
# False