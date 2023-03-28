T = [10, 20, 15, 5, 25]
from math import inf
# def sumPartition(T,s1,s2,i):
#     if i == 0:
#         return min(abs(s1+T[0]-s2),abs(s2+T[0]-s1))
#     return min(sumPartition(T,s1,s2+T[i],i-1),sumPartition(T,s1+T[i],s2,i-1))
# print(sumPartition(T,0,0,len(T)-1))

def sumPartition(T,DP,s1,s2,i):
    if i == 0:
        DP[0][s1] = min(abs(s1+T[0]-s2),abs(s2+T[0]-s1))
        return DP[0][s1]
    if DP[i][s1] != -1:
        return DP[i][s1]
    DP[i][s1] = min(sumPartition(T,DP,s1,s2+T[i],i-1),sumPartition(T,DP,s1+T[i],s2,i-1))
    return DP[i][s1]
a = sum(T)
DP = [[-1 for j in range(a+1)] for i in range(len(T))]
print(sumPartition(T,DP,0,0,len(T)-1))

def sum_partition_ite(T):
    a = sum(T)
    n = len(T)
    F = [[inf for j in range(a+1)] for _ in range(n+1)]

    #a-F[i][j] -> suma w drugim kontenerze
    for i in range(n+1):
        F[i][0] = a
    for i in range(1,n):
        for j in range(1,a+1):
            F[i][j] = F[i-1][j]
            if j - T[i] >= 0:
                F[i][j] =min(abs(F[i-1][j]))
