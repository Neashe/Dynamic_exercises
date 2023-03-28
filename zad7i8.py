from math import inf
def shortest_supersequence(X,Y,i,j,F):
    if i == 0 or j == 0:
        F[i][j] =i+j
        return i+j
    if F[i][j] !=-1:
        return F[i][j]
    if X[i-1]==Y[j-1]:
        F[i][j] = shortest_supersequence(X,Y,i-1,j-1,F)+1
        return F[i][j]
    else:
        F[i][j] = min(shortest_supersequence(X,Y,i-1,j,F)+1,shortest_supersequence(X,Y,i,j-1,F)+1)
        return F[i][j]
DP = [[-1 for i in range(7)] for _ in range(8)]
print(shortest_supersequence("ABCBDAB","BDCABA",7,6,DP))

def shortest_subsequence_ite(X,Y):
    n = len(X)
    m = len(Y)
    F = [[inf for j in range(m+1)] for _ in range(n+1)]
    for i in range(n+1):
        F[i][0] = i
    for j in range(m+1):
        F[0][j] = j
    for i in range(1,n+1):
        for j in range(1,m+1):
            if X[i-1]==Y[j-1]:
                F[i][j] = F[i-1][j-1]+1
            else:
                F[i][j]=min(F[i-1][j],F[i][j-1])+1
    return F

def find_subsequence(X,Y,F,i,j):
    if i ==0:
        return {Y[:j]}
    if j ==0:
        return {X[:i]}
    if X[i-1]==Y[j-1]:
        scs = find_subsequence(X,Y,F,i-1,j-1)
        return {s + X[i-1] for s in scs}
        # return find_subsequence(X,Y,F,i-1,j-1)+X[i-1]
    else:
        if F[i-1][j] == F[i][j-1]:
            return find_subsequence(X,Y,F,i-1,j),find_subsequence(X,Y,F,i,j-1)
        if F[i-1][j]<F[i][j-1]:
            scs = find_subsequence(X,Y,F,i-1,j)
            return{s+X[i-1] for s in scs}
            # return find_subsequence(X,Y,F,i-1,j)+X[i-1]
        else:
            scs = find_subsequence(X,Y,F,i,j-1)
            return {s+Y[j-1] for s in scs}
            # return find_subsequence(X,Y,F,i,j-1)+Y[j-1]


# print(shortest_subsequence_ite("ABCBDAB","BDCABA"))
print(find_subsequence("FABCBDAB","BDCABA",shortest_subsequence_ite("FABCBDAB","BDCABA"),8,6))

