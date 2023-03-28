"""coin change - all possible combinations"""
from math import inf
def coinChange(C,F,change,i):
    if i < 0:
        if change == 0: #solution was found
            return 1
        else:
            return 0
    if F[i][change] != -1:
        return F[i][change]
    if change-C[i] >=0:
        F[i][change] = coinChange(C,F,change-C[i],i)+coinChange(C,F,change,i-1)
        return F[i][change]
    else:
        F[i][change]= coinChange(C,F,change,i-1)
        return F[i][change]

S = [ 1, 3, 5, 7 ]
num = 8
F = [[-1 for j in range(num+1)] for i in range(len(S))]
print(coinChange(S,F,num,len(S)-1))

def coinChangeCount(S,change):
    n = len(S)
    F = [[0 for j in range(change+1)] for i in range(n+1)]
    for i in range(n+1):
        F[i][0] = 1

    for i in range(1,n+1):
        for j in range(1,change+1):
            if j - S[i-1] >=0:
                F[i][j] = F[i-1][j]+F[i][j-S[i-1]]
            else:
                F[i][j] = F[i-1][j]
    return F[n][change]

print(coinChangeCount(S,num))