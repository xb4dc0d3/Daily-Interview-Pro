'''
Hi, here's your problem today. This problem was recently asked by Amazon:

Given a non-negative integer n, convert the integer to hexadecimal and return the result as a string. 
Hexadecimal is a base 16 representation of a number, where the digits are 0123456789ABCDEF. 
Do not use any builtin base conversion functions like hex.

Here's an example and some starter code.
'''

def to_hex(n) -> str:
    res = ""
    num_in_hex = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
    while n!=0:
        
        rem = n % 16
        n = n // 16

        if rem in num_in_hex.keys():
            res += str(num_in_hex[rem])

        else:
            res += str(rem)
        
    return res[::-1]
  
print(to_hex(673))
# 7B

# 123 / 16 = 7 sisa 11
# 7 / 16 = 0 sisa 7

# 69 / 16 = 4 sisa 5