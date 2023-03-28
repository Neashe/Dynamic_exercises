"""grid_traveler"""

def grid_travel(M,i,j,DP):
    if DP[i][j]!=-1:
        return DP[i][j]
    if i == 0 and j == 0:
        DP[0][0] = M[0][0]
        return M[0][0]
    elif i >0 and j> 0:
        DP[i][j] = min(grid_travel(M, i - 1, j,DP) + M[i][j], grid_travel(M, i, j - 1,DP) + M[i][j])
        return DP[i][j]
    elif i >0:
        DP[i][j] = grid_travel(M,i-1,j,DP)+M[i][j]
        return DP[i][j]
    elif j > 0:
        DP[i][j] = grid_travel(M,i,j-1,DP)+M[i][j]
        return DP[i][j]

cost = [
        [4, 7, 8, 6, 4],
        [6, 7, 3, 9, 2],
        [3, 8, 1, 2, 4],
        [7, 1, 7, 3, 7],
        [2, 9, 8, 9, 3]
    ]
DP = [[-1 for j in range(len(cost[0]))] for _ in range(len(cost))]
print(grid_travel(cost,len(cost)-1,len(cost[0])-1,DP))
