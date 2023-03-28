def LCS_rek(word1,word2,i,j):
    if i == len(word1) or j == len(word2):
        return 0
    if word1[i] == word2[j]:
        return LCS_rek(word1,word2,i+1,j+1)+1
    else:
        return max(LCS_rek(word1,word2,i+1,j),LCS_rek(word1,word2,i,j+1))
word1 = "ABBCABCA"
word2="ADDBABGA"
print(LCS_rek(word1,word2,0,0))

def LCS_rek_dyn(word1,word2,i,j,DP):
    if DP[i][j] != -1:
        return DP[i][j]
    if i == len(word1) or j == len(word2):
        return 0
    if word1[i] == word2[j]:
        DP[i][j] = LCS_rek(word1,word2,i+1,j+1)+1
        return DP[i][j]
    else:
        DP[i+1][j] =LCS_rek(word1,word2,i+1,j)
        DP[i][j+1] = LCS_rek(word1,word2,i,j+1)
        return max(DP[i+1][j],DP[i][j+1])
T = [[-1 for j in range(len(word2))] for i in range(len(word1))]
print(LCS_rek_dyn(word1,word2,0,0,T))

def LCS_ite_dyn(word1,word2):
    n = len(word1)
    m = len(word2)
    F = [[0 for j in range(m)] for _ in range(n)]
    if word1[0] == word2[0]:
        F[0][0]=1
    for i in range(n):
        F[i][0] = F[0][0]
    for i in range(1,n):
        for j in range(1,m):
            if word1[i]==word2[j]:
                F[i][j] = F[i-1][j-1]+1
            else:
                F[i][j] = max(F[i-1][j],F[i][j-1])
    # return F[n-1][m-1]
    """printing LCS"""
    i= n-1
    j = m-1
    answer =""
    while i >0 and j > 0:
        if F[i-1][j]==F[i][j-1] and F[i-1][j-1] == F[i][j]-1:
            answer += word2[j]
            i=i-1
            j=j-1
        elif F[i-1][j] > F[i][j-1]:
            i=i-1
        else:
            j=j-1
    if F[i][j] ==1:
        answer+=word2[j]
    return answer[::-1]




print(LCS_ite_dyn(word1,word2))
