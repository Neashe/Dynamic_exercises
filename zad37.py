"""An island is in the form of a square matrix, and a person is standing inside the matrix.
The person can move one step in any direction (right, left, top, down) in the matrix.
 Calculate the probability that the person is alive after walking n steps on the island,
 provided that the person dies on stepping outside the matrix."""
def dead(x,i,j):
    return i < 0 or i >=x or j < 0 or j >= x

def deathProbability(F,x,i,j,n):
    if dead(x,i,j):
        return (1,0)
    if n == 0:
        return (0,1)
    if F[i][j][n] != -1:
        return F[i][j][n]
    F[i][j][n] = ((deathProbability(F,x,i-1,j,n-1)[0]+ deathProbability(F,x,i+1,j,n-1)[0]\
    +deathProbability(F,x,i,j-1,n-1)[0]+deathProbability(F,x,i,j+1,n-1)[0])/4,(deathProbability(F,x,i-1,j,n-1)[1]+
    deathProbability(F,x,i+1,j,n-1)[1]\
    +deathProbability(F,x,i,j-1,n-1)[1]+
    deathProbability(F,x,i,j+1,n-1)[1])/4)
    return F[i][j][n]

def deathProbabilityAns(x,n,a,b):
    F = [[[-1 for k in range(n + 1)] for j in range(x)] for i in range(x)]
    deaths,lifes = deathProbability(F,x,a,b,n)
    return lifes/(deaths+lifes)*100

print(deathProbabilityAns(3,1,1,1))




