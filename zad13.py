M =  [[0 ,  0  , 1 ,  0  , 1 ,  1],
      [0,   1,   1,   1,   0,   0],
      [0 ,  0 ,  1 ,  1 ,  1,   1],
      [1,   1,   0 ,  1 ,  1,   1],
      [1,   1,   1,   1,   1,   1],
      [1,   1,   0,   1,   1,   1],
      [1,   0,   1,   1,   1,   1],
      [1,   1,   1,   0,   1,   1]]
def largestBinSquare(M):
    n = len(M)
    m = len(M[0])
    F = [[0 for j in range(m)]for _ in range(n)]
    max_square = 0
    for i in range(n):
        if M[i][0]:
            F[i][0] = 1
    for j in range(1,m):
        if M[0][j]:
            F[0][j] = 1
    for i in range(1,n):
        for j in range(1,m):
            if M[i][j]:
                F[i][j] = min(F[i-1][j-1],F[i-1][j],F[i][j-1])+1
                max_square = max(max_square,F[i][j])
    return max_square

print(largestBinSquare(M))


