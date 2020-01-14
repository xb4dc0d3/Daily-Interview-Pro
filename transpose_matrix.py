'''
Hi, here's your problem today. This problem was recently asked by Twitter:

Given a matrix, transpose it. Transposing a matrix means the rows are now the column and vice-versa.

Here's an example:
'''

def transpose(mat):
    column = len(mat[0])
    row = len(mat)
    result = [[0 for i in range(row)] for j in range(column)]

    for i in range(row):
        for j in range(column):
            result[j][i] = mat[i][j]

    return result

mat = [
    [1, 2, 3],
    [4, 5, 6],
]

print(transpose(mat))
# [[1, 4],
#  [2, 5], 
#  [3, 6]]