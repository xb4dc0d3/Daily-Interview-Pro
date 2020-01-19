'''
Hi, here's your problem today. This problem was recently asked by AirBNB:

Pascal's Triangle is a triangle where all numbers are the sum of the two numbers above it. 
Here's an example of the Pascal's Triangle of size 5.

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1

Given an integer n, generate the n-th row of the Pascal's Triangle.

Here's an example and some starter code.
'''

def pascal_triangle_row(n):

  n = n-1 # indexing start with 1
  list_n_row = [1] # each row, always number 1
  for jj in range(n):
    list_n_row.append(int(list_n_row[jj]*(n-jj)/(jj+1)))
  
  return list_n_row

print(pascal_triangle_row(6))
# [1, 5, 10, 10, 5, 1]