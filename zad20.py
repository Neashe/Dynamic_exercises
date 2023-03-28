def partition_problem(T,first,second,i):
    if sum(T) % 2 == 1:
        return 0
    if i == 0:
        return (T[0]+first==second or T[0]+second == first)
    return partition_problem(T,first+T[i],second,i-1) or partition_problem(T,first,second+T[i],i-1)
def equal_partition_problem(T,F,container,i):
    if sum(T) %2 ==1:
        return 0
    if container == sum(T)//2:
        return 1
    if i < 0:
        return 0
    F[i] = equal_partition_problem(T,F,container+T[i],i-1) or equal_partition_problem(T,F,container,i-1)
    return F[i]

nums = [7, 3, 1, 5, 4, 8]
print(partition_problem(nums,0,0,len(nums)-1))
F = [-1 for j in range(sum(nums)//2)]
print(equal_partition_problem(nums,F,0,len(nums)-1))