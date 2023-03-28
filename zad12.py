"""edit_string"""
from math import inf
def edit_string(X,Y):
    m = len(X)
    n = len(Y)
    F = [[inf for j in range(m)] for _ in range(n)]
    if X[0]==Y[0]:
        F[0][0] = 0
    else:
        F[0][0] = 1
    for i in range(1,m):
        F[0][i] = F[0][i-1]+1
    for i in range(1,n):
        F[i][0] = F[i-1][0]+1

    for i in range(1,n):
        for j in range(1,m):
            if X[j] == Y[i]:
                F[i][j] = F[i-1][j-1]
            else:
                F[i][j] = min(F[i][j-1],F[i-1][j],F[i-1][j-1])+1
    return F[n-1][m-1]

a = "kitten"
b = "sitting"
print(edit_string(a,b))