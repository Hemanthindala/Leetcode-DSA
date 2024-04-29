def minOperations(nums,k):
    res=0
    for i in range(len(nums)):
        res=res^nums[i]
    res=res^k
    count=0
    while(res>0):
        count=count+res%2
        res=res//2
    return count

#Link: https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/description/?envType=daily-question&envId=2024-04-26
#Video Solution: https://www.youtube.com/watch?v=OQ8KuCvtFfs
