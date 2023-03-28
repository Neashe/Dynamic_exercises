def repeated_LCS(X,i,j):
    if i == len(X) or  j ==len(X):
        return 0
    if X[i]==X[j] and i !=j:
        return repeated_LCS(X,i+1,j+1)+1
    else:
        return max(repeated_LCS(X,i+1,j),repeated_LCS(X,i,j+1))
def repeated_LCS_dyn_rek(X,i,j,F):
    if i ==len(X) or j ==len(X):
        return 0
    if F[i][j] != -1:
        return F[i][j]
    if X[i]==X[j] and i != j:
        F[i][j] = repeated_LCS_dyn_rek(X,i+1,j+1,F)+1
        return F[i][j]
    else:
        F[i][j] = max(repeated_LCS_dyn_rek(X,i+1,j,F),repeated_LCS_dyn_rek(X,i,j+1,F))
        return F[i][j]

def repeated_LCS_ite(X):
    n = len(X)
    F=[[0 for i in range(n+1)] for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,n+1):
            if X[i-1] == X[j-1] and i != j:
                F[i][j] = F[i-1][j-1]+1
            else:
                F[i][j]=max(F[i-1][j],F[i][j-1])
    return F
def print_repeated_LCS(X,F,i,j):
    if i == 0 or j == 0:
        return ""
    if F[i-1][j]== F[i][j-1] and F[i-1][j-1]+1==F[i][j]:
        return print_repeated_LCS(X,F,i-1,j-1)+X[i-1]
    else:
        if F[i-1][j] > F[i][j-1]:
            return print_repeated_LCS(X,F,i-1,j)
        else:
            return print_repeated_LCS(X,F,i,j-1)

word="ATACTCGGA"
print(repeated_LCS(word,0,0))
DP = [[-1 for i in range(len(word))] for _ in range(len(word))]
print(repeated_LCS_dyn_rek(word,0,0,DP))
# print(repeated_LCS_ite(word))
print(print_repeated_LCS(word,repeated_LCS_ite(word),len(word),len(word)))