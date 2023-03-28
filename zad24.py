"""rod cutting"""

def rodCut(T,P,i,l):
    if i < 0:
        return 0
    if l-T[i]>=0:
        return max(rodCut(T,P,i-1,l-T[i])+P[i],rodCut(T,P,i-1,l),rodCut(T,P,i,l-T[i])+P[i])
    else:
        return rodCut(T,P,i-1,l)
def rodCutIte(P,rod):
    T = [0 for i in range(rod+1)]
    for i in range(1,rod+1):
        for j in range(1,i+1):
            T[i] = max(T[i],P[j-1]+T[i-j])
    return T[rod]

length = [1, 2, 3, 4, 5, 6, 7, 8]
price = [1, 5, 8, 9, 10, 17, 17, 20]
l = 4
print(rodCut(length,price,len(length)-1,l))
print(rodCutIte(price,l))
