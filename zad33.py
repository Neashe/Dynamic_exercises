"""word break"""
#
# def wordBreak(T,F,word,i):
#     if word == "":
#         return True
#     if i ==len(T):
#         return False
#     if F[len(word)-1] != -1:
#         return F[len(word)]
#     if T[i] == word[0:len(T[i])]:
#         F[len(word)-1] = wordBreak(T,F,word[i::],i+1) or wordBreak(T,F,word,i+1)
#         return F[len(word)-1]
#     else:
#         F[len(word)-1] = wordBreak(T,F,word,i+1)
#         return F[len(word)-1]
def wordBreaks(words, word, out=''):
    # if the end of the string is reached,
    # print the output string
    if not word:
        print(out)
        return

    for i in range(1, len(word) + 1):
        # consider all prefixes of the current string
        prefix = word[:i]

        # if the prefix is present in the dictionary, add it to the
        # output string and recur for the remaining string
        if prefix in words:
            wordBreaks(words, word[i:], out + ' ' + prefix)

def wordBreakIte(W,word):
    n = len(word)
    F = [False for i in range(n+1)]
    F[0] = True
    for i in range(n):
        for j in W:
            if  F[i] and word[i] == j[0] and i+len(j)<n+1:
                F[i+len(j)] = True
    return F[n]
from math import inf
def wordBreak(T,F,word,i):
    if word == "":
        return 1
    if i ==len(T):
        return inf
    if F[len(word)-1] != -1:
        return F[len(word)]
    if T[i] == word[0:len(T[i])]:
        F[len(word)-1] = min(wordBreak(T,F,word[i::],i+1)+1,wordBreak(T,F,word,i+1))
        return F[len(word)-1]
    else:
        F[len(word)-1] = wordBreak(T,F,word,i+1)
        return F[len(word)-1]
words = [
    'self', 'th', 'is', 'famous', 'Word', 'break', 'b', 'r',
    'e', 'a', 'k', 'br', 'bre', 'brea', 'ak', 'problem'
]
# input string
word = 'Wordbreakproblem'
F = [-1 for i in range(len(word))]
print(wordBreak(words,F,word,0))
print(wordBreakIte(words,word))

