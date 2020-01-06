'''
Hi, here's your problem today. This problem was recently asked by Microsoft:

N-Queens is the problem where you find a way to put n queens on a nxn chess board \
    without them being able to attack each other. 

Given an integer n, return 1 possible solution by returning all the queen's position.

'''

# Print state of queens game
def stateGame(board, n):
    data = []
    for i in range(n):
        for j in range(n):
            # board[i][j] represents queen position
            if board[i][j] == 1: 
                print("Q", end=" ")
            else: 
                print(".", end=" ")
        print()

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                data.append((i,j))
    print(data)


def isSafeState(n, board, row, col):

    # Check row on same side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solver(n, board, col):

    # Base case if all queen are in the right place
    if col >= n: 
        return True

    for i in range(n):

        if isSafeState(n, board, i, col):
            board[i][col] = 1
            
            if solver(n, board, col+1) == True:
                return True

            # if not found, then try another board[i][col]
            board[i][col] = 0

    return False


def n_queens(n):
    board = [[0 for x in range(n)] for x in range(n)] # init board

    if solver(n, board, 0) == False:
        return "Not solution exists."

    stateGame(board,n)

    return "There's a solution exists."

print(n_queens(5))
# There can be many answers
# [(0, 0), (1, 2), (2, 4), (3, 1), (4, 3)]

# Q . . . .
# . . . Q .
# . Q . . .
# . . . . Q
# . . Q . .