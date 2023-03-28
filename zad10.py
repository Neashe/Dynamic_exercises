def longest_incresing_seq(T):
    n = len(T)
    F = [0 for i in range(n)]
    for i in range(1,n):
        for j in range(i):
            if T[j] < T[i] and F[j] > F[i]:
                F[i] = F[j]
        F[i] = F[i]+1
    answer = 0
    for i in range(n):
        answer = max(answer,F[i])
    return F
def longest_descreasing_seq(T):
    n = len(T)
    F = [0 for i in range(n)]
    # F[n-1] = 1
    for i in range(n-1,-1,-1):
        maxim = F[i]
        for j in range(n-1,i-1,-1):
            if T[j] < T[i]:
                maxim = max(maxim,F[j])
        F[i] = maxim+1
    answer = 0
    for i in range(n):
        answer = max(answer,F[i])
    return F

def bitonic_seq(T):
    A = longest_incresing_seq(T)
    B = longest_descreasing_seq(T)
    max_idx = 0
    max_sq = 0
    for i in range(len(T)):
        if A[i]+B[i]-1 > max_sq:
            max_sq = A[i]+B[i]-1
            max_idx = i
    I = [[] for i in range(len(T))]
    D = [[] for j in range(len(T))]
    I[0].append(T[0])

    D[0].insert(0,T[len(T)-1])
    for i in range(1,len(T)):
        for j in range(i):
            if T[j]<T[i] and len(I[i])<len(I[j]):
                I[i] = I[j].copy()
        I[i].append(T[i])
    for i in range(len(T)-1,-1,-1):
        for j in range(len(T)-1,i-1,-1):
            if T[j] < T[i] and len(D[i])<len(D[j]):
                D[i] = D[j].copy()
        D[i].insert(0,T[i])
    for i in I[max_idx]:
        print(i,end=" ")
    for i in D[max_idx][1:]:
        print(i,end=" ")



    return 7

T = [4, 2, 5, 9, 7, 6, 10, 3, 1]
bitonic_seq(T)

