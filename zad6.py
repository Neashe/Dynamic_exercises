"""diff utility"""

def LCS(X,Y):
    n = len(X)
    m= len(Y)
    F = [[0 for j in range(m+1)]for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if X[i-1]==Y[j-1]:
                F[i][j]=F[i-1][j-1]+1
            else:
                F[i][j]=max(F[i-1][j],F[i][j-1])
    return F
def print_LCS(X,Y,i,j,F):
    if i == 0 or j == 0:
        return ""
    if X[i-1]==Y[j-1]:
        return print_LCS(X,Y,i-1,j-1,F)+X[i-1]
    else:
        if F[i-1][j]>F[i][j-1]:
            return print_LCS(X,Y,i-1,j,F)
        else:
            return print_LCS(X,Y,i,j-1,F)


x= "XMJYAUZ"
y = "QXMJAATZ"
def diff_utility(x,y,i,j,core):
    if i > 0 and j >0 and x[i-1]==y[j-1]:
        diff_utility(x,y,i-1,j-1,core[0:-1])
        print(x[i-1],end=" ")
    elif j > 0 and core !="" and (core[-1] != y[j-1]):
        diff_utility(x,y,i,j-1,core)
        print("+"+y[i-1],end=" ")
    elif i > 0 and core !="" and(core[-1] != x[i-1]):
        diff_utility(x,y,i-1,j,core)
        print("-"+x[i-1],end=" ")

diff_utility(x,y,len(x),len(y),print_LCS(x,y,len(x),len(y),LCS(x,y)))


