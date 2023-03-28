def LPS(word):
    n = len(word)
    F = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        F[i][i] = 1
    k=0
    while k<len(word)-1:
        for i in range(n-1-k):
            j = i+1+k
            if word[i]==word[i+1+k]:
                if k==1:
                    F[i][j] = max(F[i + 1][j], F[i][j - 1]) + 2
                else:
                    F[i][j] = max(F[i + 1][j], F[i][j - 1]) + 1
            else:
                F[i][j] = max(F[i + 1][j], F[i][j - 1])
        k+=1
    return F[0][len(word)-1]

def LPS_rek(X,i,j,DP):
    if i > j:
        return 0
    if DP[i][j] != -1:
        return DP[i][j]
    if i == j:
        DP[i][j]= 1
        return 1
    if X[i]==X[j]:
        DP[i][j] = LPS_rek(X,i+1,j-1,DP) +2
        return DP[i][j]
    else:
        DP[i][j] = max(LPS_rek(X,i+1,j,DP),LPS_rek(X,i,j-1,DP))
        return DP[i][j]
def LPS_bad(X,i,j):
    if i >j:
        return 0
    if i == j:
        return 1
    if X[i]==X[j]:
        return LPS_bad(X,i+1,j-1)
    else:
        return max(LPS_bad(X,i+1,j),LPS_bad(X,i,j-1))
X="ananas"
Y = "abbdcacb"
# print(LPS(X))
print(LPS(Y))

DP2 = [[-1 for k in range(len(Y))] for _ in range(len(Y))]

print(LPS_rek(Y,0,len(Y)-1,DP2))
X = "abshsbshsfffdpsssdmshdksusjshbrmdjbdhfdpoeitbyhdythflsoedbdhstemdhfhrlsh"
DP = [[-1 for i in range(len(X))] for j in range(len(X))]
print(LPS_rek(X,0,len(X)-1,DP))
print(LPS_bad(X,0,len(X)-1))




