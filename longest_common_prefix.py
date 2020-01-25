'''
Hi, here's your problem today. This problem was recently asked by Microsoft:

Given a list of strings, find the longest common prefix between all strings.

Here's some examples and some starter code.
'''

def longest_common_prefix(strs) -> str:
    res = ""
    if not strs:
        print(" ")
        return 0

    minim = min([len(item) for item in strs])  # check the shortest length

    ii = 0
    while ii < minim:
        check = strs[0][ii]
        for item in strs:
            if item[ii] != check:
                return res
        res += check
        ii += 1
    return res


print(longest_common_prefix(['helloworld', 'hellokitty', 'hell']))
# hell

print(longest_common_prefix(['daily', 'interview', 'pro']))
# ''
