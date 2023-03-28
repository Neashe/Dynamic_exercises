"""Given an M × N integer matrix, calculate the maximum sum submatrix of size k × k in
it in O(M × N) time. Here, 0 < k < M <= N."""
#O(M*N)
def matrixPreprocessing(M):
    prep = [[0 for j in range(len(M[0]))] for i in range(len(M))]
    prep[0][0] = M[0][0]
    for i in range(1,len(M)):
        prep[i][0] = M[i][0]+prep[i-1][0]
    for j in range(1,len(M[0])):
        prep[0][j] = M[0][j]
    for i in range(1,len(M)):
        for j in range(1,len(M[0])):
            prep[i][j] = prep[i - 1][j] + prep[i][j - 1] - prep[i - 1][j - 1] + M[i][j]
    return prep
#O(NxM)
def maxSubmatrixSum(M,k):
    sum_matrix = matrixPreprocessing(M)
    maxSum = 0
    idx = (k-1,k-1)
    for i in range(k-1,len(M)):
        for j in range(k-1,len(M[0])):
            total = sum_matrix[i][j]
            if i - k >= 0:
                total -= sum_matrix[i-k][j]
            if j - k >= 0:
                total -= sum_matrix[i][j-k]
            if i-k >= 0 and j-k >=0:
                total += sum_matrix[i-k][j-k]
            if total > maxSum:
                maxSum = total
                idx = (i,j)
    return [[mat[idx[0]-k+1+y][idx[1]-k+1+x] for x in range(k)] for y in range(k)]


mat = [
    [3, -4, 6, -5, 1],
    [1, -2, 8, -4, -2],
    [3, -8, 9, 3, 1],
    [-7, 3, 4, 2, 7],
    [-3, 7, -5, 7, -6]
]
# submatrix size
k = 3
print(maxSubmatrixSum(mat,k))