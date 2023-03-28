def matrix_seq(M,i,j):
    if i>0 and i < len(M) and j >0 and j < len(M[0]):
        maxim = 0
        x = M[i-1][j]
        y = M[i][j-1]
        z = M[i+1][j]
        w = M[i][j+1]
        matrix_seq(M,i-1,j)
        matrix_seq(M,i,j-1)
        matrix_seq(M,i+1,j)
        matrix_seq(M,i,j+1)
        