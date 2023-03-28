"""Given an M × N matrix where each cell can have a value of 1, 0, or -1,
 where -1 denotes an unsafe cell, collect the maximum number of ones starting
 from the first cell and by visiting only safe cells (i.e., 0 or 1).
 We can only go left or down if the row is odd; otherwise, # if i %2 == 1
  we can only go right or down from the current cell."""
def isNotSafe(mat, i, j):
    return i < 0 or i >= len(mat) or j < 0 or j >= len(mat[0]) or mat[i][j] == -1
def matrix_travel(M,F,i,j):
    if isNotSafe(M,i,j):
        return 0
    if F[i][j] != -1:
        return F[i][j]
    if i % 2 == 1:
        #left or down
        F[i][j] = max(matrix_travel(M,F,i+1,j),matrix_travel(M,F,i,j-1) )+M[i][j]
        return F[i][j]
    else:
        F[i][j] = max(matrix_travel(M, F, i + 1, j),matrix_travel(M,F,i,j+1))+M[i][j]
        return F[i][j]


mat = [
        [1, 1, -1, 1, 1],
        [1, 0, 0, -1, 1],
        [1, 1, 1, 1, -1],
        [-1, -1, 1, 1, 1],
        [1, 1, -1, -1, 1]
    ]
F = [[-1 for j in range(len(mat[0]))] for i in range(len(mat))]
print(matrix_travel(mat,F,0,0))

