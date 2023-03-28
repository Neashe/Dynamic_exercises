"""maxim_ascending_sum
    MSIS"""

def max_sum(T):
    n = len(T)
    F = [0 for i in range(n)]
    F[0] = T[0] #pierwszy element ma maksymalną sumę równą sobie

    for i in range(1,n):
        for j in range(i):
            if T[j]<T[i] and F[i] < F[j]:
                F[i]=F[j]
        F[i] += T[i]
    #szukanie największej sumy
    max_sum = 0
    for i in range(n):
        max_sum= max(max_sum,F[i])
    return max_sum
def print_MSIS(T):
    n = len(T)
    I = [[]for i in range(n)]
    I[0].append(T[0])
    for i in range(1,n):
        for j in range(n):
            if T[j]<T[i] and len(I[i])<len(I[j]):
                I[i]=I[j].copy()
        I[i].append(T[i])
    return I

T = [8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11]
print(max_sum(T))
print(print_MSIS(T))