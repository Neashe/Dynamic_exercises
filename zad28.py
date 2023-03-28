"""longest alternating sub"""

def alter_sub(T,F,direction,prev,i): #ending with index i
    pass

def altereting(T):
    n = len(T)
    F = [0 for i in range(n)]
    flags = [-1 for i in range(n)]
    F[0] = 1
    F[1] = 2
    flag = 0
    if T[1] > T[0]:
        flags[1] = 1
    for i in range(2,n):
        flags[i] = int(T[i]>T[0])
        F[i] = 2
        for j in range(1,i):
            if (flags[j] == 1 and T[j] < T[i]) or (flags[j] == 0 and T[j] > T[i]):
                F[i] = max(F[i],F[j]+1)
                flags[i] = flags[j] % 2 + 1
    answer = 1
    for i in range(1,n):
        answer = max(answer,F[i])
    return answer
A = [8, 9, 6, 4, 5, 7, 3, 2, 4]
print(altereting(A))

def alteretings(T):
    n = len(T)
    F = [[-1]*2 for i in range(n)]
    F[0][0] = 1
    F[0][1] = 1
    answer = 0
    for i in range(1,n):
        for j in range(i):
            if T[j] < T[i]:
                F[i][1] = max(F[i][1],F[j][0]+1)
            elif T[j] > T[i]:
                F[i][0] = max(F[i][0],F[j][1]+1)
            answer = max(answer,F[i][0],F[i][1])
    return answer
print(alteretings(A))




