"""linear equation"""

def linEq(T,num,i):
    if num == 0:
        return 1
    if i < 0:
        return 0
    if T[i]<=num:
        return linEq(T,num,i-1)+linEq(T,num-T[i],i)
    else:
        return linEq(T,num,i-1)

def linEqDYN(T,F,num,i):
    if num == 0:
        return 1
    if i < 0:
        return 0
    if F[i][num] != -1:
        return F[i][num]
    if T[i]<=num:
        F[i][num]= linEqDYN(T,F,num,i-1)+linEqDYN(T,F,num-T[i],i)
        return F[i][num]
    else:
        F[i][num]= linEqDYN(T,F,num,i-1)
        return F[i][num]
coeff = [1, 3, 5, 7,2,5,9,4,6,7,8,4,12,4,5,6,11,13,14,15,16,17,4,3,6,8,5,9,4,6,7,8,4,12,4,5,5,9,4,6,7,8,4,12,4,5,6,11,13,14,15,16,17,4,3,6,8,5,6,3,4,6,3,5,3,9,86,11,13,14,15,16,17,4,3,6,8,5,6,3,4,6,3,5,3,9,85,6,3,4,6,3,5,3,9,8,6,7,5,9,4,6,7,8,4,12,4,5,6,11,13,14,15,16,17,4,3,6,8,5,6,3,4,6,3,5,3,9,8]
rhs = 28
# print(linEq(coeff,rhs,len(coeff)-1))
numb = [1,2,3]
print(linEq(numb,4,len(numb)-1))
F = [[-1 for j in range(rhs+1)] for i in range(len(coeff))]
print(linEqDYN(coeff,F,rhs,len(coeff)-1))