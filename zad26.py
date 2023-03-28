"""coin change problem"""
from math import inf
# def coinChange(C,change,i):
#     if i < 0:
#         if change == 0:
#             return 0
#         else:
#             return inf
#     if change-C[i] >=0:
#         return min(coinChange(C,change-C[i],i)+1,coinChange(C,change-C[i],i-1)+1,coinChange(C,change,i-1))
#     else:
#         return coinChange(C,change,i-1)

coins = [1, 3, 5, 7]
change = 345
# print(coinChange(coins,change,len(coins)-1))

def coinChange(C,F,change,i):
    if i < 0:
        if change == 0:
            return 0
        else:
            return inf
    if F[i][change] != -1:
        return F[i][change]
    if change-C[i] >=0:
        F[i][change] = min(coinChange(C,F,change-C[i],i)+1,coinChange(C,F,change,i-1))
        return F[i][change]
    else:
        F[i][change]= coinChange(C,F,change,i-1)
        return F[i][change]

F = [[-1 for j in range(change+1)] for i in range(len(coins))]
print(coinChange(coins,F,change,len(coins)-1))

def coinChangeIte(C,change):
    n = len(C)
    F = [[inf for j in range(change+1)] for i in range(n)]
    F[0][0] = 0
    for i in range(n):
        F[i][0] = 0
    for j in range(1,change+1):
        if j % C[0]:
            F[0][j] = j //C[0]

    for i in range(1,n):
        for j in range(1,change+1):
            if j-C[i] >=0:
                F[i][j] = min(F[i-1][j],F[i][j-C[i]]+1,F[i][j]+1)
            else:
                F[i][j] = F[i-1][j]
    return F[n-1][change]

print(coinChangeIte(coins,18))
