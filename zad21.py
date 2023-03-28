"""subset sum"""

def subset_sum(T,k):
    F= [0 for i in range(k+1)]
    F[0] = 1
    for i in range(k+1):
        for j in range(len(T)):
            if F[i] and i+T[j]<=k and i !=T[j]:
                F[i+T[j]] = 1
    return F[k]
A = [ 7, 3, 2, 5, 8 ]
key = 14
print(subset_sum(A,key))