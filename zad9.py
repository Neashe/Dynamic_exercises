def longest_seq(T):
    n = len(T)
    F = [1 for i in range(n)]
    for i in range(1,n):
        maxim = F[i]
        for j in range(i):
            if T[j] < T[i]:
                maxim = max(maxim,F[j])
        F[i] = maxim+1
    answer = 0
    for i in range(n):
        answer = max(answer,F[i])
    return F
T = [1,5,6,3,2,4,89,6,7,4,3,24,10,9,10]
# print(longest_seq(T))
arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
# print(longest_seq(arr))

def print_LIS(T,F,i,curr):
    if F[curr] == 1:
        print(T[curr],end=" ")
        return
    if F[i]+1 == F[curr] and T[i]<T[curr]:
        print_LIS(T,F,i-1,i)
        print(T[curr],end =" ")
    else:
        print_LIS(T,F,i-1,curr)

print_LIS(T,longest_seq(T),len(T)-2,len(T)-1)
