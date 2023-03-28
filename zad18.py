"""0-1 knapsack problem"""
def knapsack_rek(W,V,w,i):
    if i ==0:
        if W[0]<=w:
            return V[0]
        else:
            return 0
    if w-W[i] >=0:
        return max(knapsack_rek(W,V,w,i-1),knapsack_rek(W,V,w-W[i],i-1)+V[i])
    else:
        return knapsack_rek(W,V,w,i-1)
value = [ 20, 5, 10, 40, 15, 25 ]
weight = [ 1, 2, 3, 8, 7, 4 ]
W = 10
print(knapsack_rek(weight,value,W,len(value)-1))
print(max(value))
F = [[-1 for j in range(max(value)+1)] for _ in range(W+1)]

def knapsack_memo(W,V,w,i,F):
    if w <0:
        return 0
    if i ==0:
        if W[0]<=w:
            return V[0]
        else:
            return 0
    if F[i][w] != -1:
        return F[i][w]
    if w - W[i] >= 0:
        return max(knapsack_memo(W,V,w,i-1,F),knapsack_memo(W,V,w-W[i],i-1,F)+V[i])
    else:
        return knapsack_memo(W,V,w,i-1,F)
print(knapsack_memo(weight,value,W,len(value)-1,F))

def knapsack_ite(W,V,w):
    n = len(V)
    max_val = max(V)
    F = [[0 for j in range(w+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,w+1):
            if j-W[i]>=0:
                F[i][j] = max(F[i-1][j]+V[i],F[i-1][j])



