"""consecutive 1's"""

def Fib(n):
    a = 2
    b = 3
    for i in range(1,n):
        a,b = b,a+b
    return a
print(Fib(3))

def CountStrings(n):
    T = [[0 for i in range(2)] for _ in range(n)]
    T[0][1] = 0
    T[0][0]= 1
    for i in range(1,n):
        T[i][0] = T[i-1][0]+T[i-1][1]
        T[i][1] = T[i-1][0]
    return T[n-1][0]
print(CountStrings(5))