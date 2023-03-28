T = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def maxSubarray(T):
    maxElement = max(T)
    if maxElement<0:
        return maxElement
    maxSub = 0
    maxSubEnd = 0
    for i in range(len(T)):
        maxSubEnd += T[i]
        maxSubEnd = max(0,maxSubEnd)
        maxSub = max(maxSubEnd,maxSub)
    return maxSub



print(maxSubarray(T))