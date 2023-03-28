"""Given a positive number n and a mobile keypad having digits from 0 to 9 associated
with each key,
 count the total possible combinations of digits having length n.
 We can start with any digit and press only four adjacent keys of any digit.
 The keypad also contains * and # keys, which we are not allowed to press."""

def notValid(M,i,j):
    return i < 0 or i >= len(M) or j < 0 or j >= len(M[0]) or M[i][j] == "*" or M[i][j] == "#"

def mobile_key(M,F,n,i,j):
    if notValid(M,i,j):
        return 0
    if F[i][j][n]!=-1:
        return F[i][j][n]
    if n == 1:
        F[i][j][n] = 1
        return 1
    F[i][j][n] = mobile_key(M,F,n-1,i,j)+mobile_key(M,F,n-1,i-1,j)+mobile_key(M,F,n-1,i,j-1)+\
           mobile_key(M,F,n-1,i+1,j)+ mobile_key(M,F,n-1,i,j+1)
    return F[i][j][n]

keypad = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['*', '0', '#']
    ]
num = 120
def mobile_keyCount(M,num):
    result = 0
    F = [[[-1 for k in range(num+1)] for y in range(len(M[0]))] for _ in range(len(M))]
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] != "#" and M[i][j]!="*":
                result += mobile_key(M,F,num,i,j)
    return result
print(mobile_keyCount(keypad,num))