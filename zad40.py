"""max sum with no adjacent elements"""
from math import inf
def maxSumAd(T):
    n = len(T)
    F = [0 for i in range(n)]
    F[0] = T[0]
    F[1] = max(T[0],T[1])
    for i in range(2,n):
        F[i] = max(F[i-1],F[i-2]+T[i])
    return F[n-1]

def maxSumRek(T,F,i):
    if i < 0:
        return 0
    if F[i] != -inf:
        return F[i]
    F[i] = max(maxSumRek(T,F,i-1),maxSumRek(T,F,i-2)+T[i])
    return F[i]


def findMaxSumSubsequence(nums):
    # base case
    if not nums:
        return 0

    # base case
    if len(nums) == 1:
        return nums[0]

    # store maximum sum until index `i-2`
    prevOfPrev = nums[0]

    # stores maximum sum until index `i-1`
    prev = max(nums[0], nums[1])

    # start from index 2
    for i in range(2, len(nums)):
        # `curr` stores the maximum sum until index `i`
        curr = max(nums[i], max(prev, prevOfPrev + nums[i]))
        prevOfPrev = prev
        prev = curr

    # return maximum sum
    return prev

long_numb = [1,-4,6,5,-8,9,-12,4,-6,-3,-6,-4,10,-11,28,7,6,6,8,-6,9,3,7,5,8,12,2,0,-8,6,7,0,0,2,6,-7,4,-8,67]
nums = [1, 2, 9, 4, 5, 0, 4, 11, 6]
Flong = [-inf for i in range(len(long_numb))]
print(maxSumAd(nums))
# print(maxSumRek(nums,5,len(nums)-1))
print(maxSumAd(long_numb))
print(maxSumRek(long_numb,Flong,len(long_numb)-1))
print(findMaxSumSubsequence(long_numb))