"""rod cut multiplication"""

def cutRod(n):
    F = [1 for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,i+1):
            F[i] = max(F[i],F[i-j]*j)
    return F[n]

print(cutRod(15))