def countPattern(string,pattern,F,i,j):
    if i < 0 and j >= 0:
        return 0
    elif j< 0:
        #pattern found
        return 1
    if F[i][j] != -1:
        return F[i][j]
    if string[i] == pattern[j]:
        F[i][j] = (countPattern(string,pattern,F,i-1,j-1)+countPattern(string,pattern,F,i-1,j))
        return F[i][j]
    else:
        F[i][j] = countPattern(string,pattern,F,i-1,j)
        return F[i][j]
string = "subsequence"
pattern = "sue"
F = [[-1 for j in range(len(pattern))] for i in range(len(string))]
# print(countPattern(string,pattern,F,len(string)-1,len(pattern)-1))
word = "abbbabbaaababababcccbaccbacbacbababcbabcbbbbaccccbacbababcbabcbbbbcbacbababcbabcbbbbacccbaabcbcabbdjkbfgjhwdsvfjksdbfkjvsdaccccbacbababcbabcbbbbacccbaabcbcabbdjkbfgjhwdsvfjksdbfkjvsdbaabcbcabbdjkbfgjhwdsvfjksdbfkjvsdcbacbababcbabcbbbbacccbaabcbcabbdjkbfgjhwdsvfjksdbfkjvsdbaabcbcabbdjkbfgjhwdsvfjksdbfkjvsdcbacbababcbabcbbbbacccbaabcbcabbdjkbfgjhwdsvfjksdbfkjvsdbabcbacbababcbabcbbbbacccbaabcbcabbdjkbfgjhwdsvfjksdbfkjvsdhvfjhsdvfjksdbfjkdvfhdvfhvdsjfbsdjkfbsdjkfvdsfvdsjhfvsdjkdfbsdbabcbaccccbababcbacbababcbabcbbbbacccbaabcbcabbababcbacbababcbabcbbbbacccbaabcbcabccbababcbacbababcbabcbbbbacccbaabcbcabcbababcbabcbbbbacccbaabcbcab"
patter = "abbaababababcccbaccbacbacbababcba"
DP = [[-1 for y in range(len(patter))] for x in range(len(word))]
# print(countPattern(word,patter,DP,len(word)-1,len(patter)-1))

