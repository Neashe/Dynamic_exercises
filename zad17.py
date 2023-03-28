def matrix_same_cost(M,i,j,cost,F):
    if cost <0:
        return 0
    if i == 0 and j == 0:
        if cost == M[0][0]:
            return 1
        return 0
    if F[i][j][cost] != -1:
        return F[i][j][cost]
    if i >0 and j >0:
        F[i][j][cost] = matrix_same_cost(M,i-1,j,cost-M[i][j],F)+matrix_same_cost(M,i,j-1,cost-M[i][j],F)
        return F[i][j][cost]
    elif i >0:
        F[i][j][cost] = matrix_same_cost(M,i-1,j,cost-M[i][j],F)
        return F[i][j][cost]
    elif j > 0:
        F[i][j][cost] = matrix_same_cost(M,i,j-1,cost-M[i][j],F)
        return F[i][j][cost]
mat = [
    [4, 7, 1, 6],
    [5, 7, 3, 9],
    [3, 2, 1, 2],
    [7, 1, 6, 3]
]
cost = 25
F = [[[-1 for j in range(cost+1)] for i in range(4)]for _ in range(4)]

print(matrix_same_cost(mat,3,3,cost,F))