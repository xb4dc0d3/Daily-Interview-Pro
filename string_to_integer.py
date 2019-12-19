'''
Hi, here's your problem today. This problem was recently asked by LinkedIn:

Given a string, convert it to an integer without using the builtin str function. 
You are allowed to use ord to convert a character to ASCII code.

Consider all possible cases of an integer. In the case where the string is not a valid integer, return None.
'''

def convert_to_int(s):

    try:
        result = 0
        if str(s)[0] == "-":
            for i in str(s[1:]):
                result = 10*result - int(i)
        else:
            for i in str(s):
                result = 10*result + int(i)
        return result

    except (TypeError, ValueError):
        return None


print(convert_to_int('-105') + 1)
# -104