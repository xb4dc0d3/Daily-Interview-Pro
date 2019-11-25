'''
Hi, here's your problem today. This problem was recently asked by Facebook:

Given an expression (as a list) in reverse polish notation, evaluate the expression. 
Reverse polish notation is where the numbers come before the operand. 
Note that there can be the 4 operands '+', '-', '*', '/'. 
You can also assume the expression will be well formed.

Example

Input: [1, 2, 3, '+', 2, '*', '-']
Output: -9

The equivalent expression of the above reverse polish notation would be (1 - ((2 + 3) * 2)).


'''

def reverse_polish_notation(expr):
    new_stack = []
    
    for i in expr:
        if isinstance(i,int):
            new_stack.append(i)
        else:
            x = new_stack.pop() # pop first
            y = new_stack.pop() # pop second
            new_stack.append(int(eval(str(y)+i+str(x))))
    
    return new_stack[0]
  
# 1 - (2 + 3) * 2
print(reverse_polish_notation([1, 2, 3, '+', 2, '*', '-']))
# -9

# (3+4) * 5
print(reverse_polish_notation([3,4,'+',5,'*']))
# 35