"""wild card characters"""

def wildCard(pattern,string,F,i,j):
    if i < 0 and j < 0:
        return True
    elif i < 0:
        return False
    elif j < 0:
        for k in range(i+1):
            if pattern[k] != "*":
                return False
        return True
    if F[i][j] != -1:
        return F[i][j]
    if pattern[i] == "*":
        F[i][j] = wildCard(pattern,string,F,i,j-1) or wildCard(pattern,string,F,i-1,j)
        return F[i][j]
    elif pattern[i] == "?":
        F[i][j]= wildCard(pattern,string,F,i-1,j-1)
        return F[i][j]
    else:
        if pattern[i] == string[j]:
            F[i][j] = wildCard(pattern,string,F,i-1,j-1)
            return F[i][j]
        else:
            return False

word = 'xyxzzxy'
pattern = 'x***y'
F = [[-1 for j in range(len(word))] for i in range(len(pattern))]
print(wildCard(pattern,word,F,len(pattern)-1,len(word)-1))