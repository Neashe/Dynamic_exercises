def common_substring(X,Y,i,j):
    if i < 0 or j < 0:
        return 0
    if X[i] == Y[j]:
        return common_substring(X,Y,i-1,j-1)+1
    else:
        return max(common_substring(X,Y,i-1,j),common_substring(X,Y,i,j-1))

def common_substring_dyn(X,Y):
    n = len(X)
    m = len(Y)
    maxLenght = 0
    F = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        if X[i]==Y[0]:
            F[i][0] = 1
    for j in range(m):
        if Y[j] == X[0]:
            F[0][j] = 1
    for i in range(1,n):
        for j in range(1,m):
            if X[i]==Y[j]:
                F[i][j]=F[i-1][j-1]+1
            maxLenght= max(F[i][j],maxLenght)
    return maxLenght

word1 = "ABABC"
word2="BABCA"
x = "samochodziarz"
y = "idkodziary"
print(common_substring(word1,word2,len(word1)-1,len(word2)-1))
print(common_substring(x,y,len(x)-1,len(y)-1))
# print(common_substring_dyn(word1,word2))
print(common_substring_dyn(x,y))