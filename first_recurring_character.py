'''
Hi, here's your problem today. This problem was recently asked by Amazon:

Given a string, return the first recurring letter that appears. If there are no recurring letters, return None.

Example:

Input: qwertty
Output: t

Input: qwerty
Output: None

'''

def first_recurring_char(s):
    length_string = len(s)

    i = 0
    while i < length_string:
        if (i+1 != length_string):
            if s[i] == s[i+1]:
                return s[i]
            else:
                i+=1
                if i == length_string:
                    return None
        
  
print(first_recurring_char('qwertty'))
# t

print(first_recurring_char('qwerty'))
# None