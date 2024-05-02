def rob(self, nums):
    rob1 = 0
    rob2 = 0
    for i in nums:
        # [rob1,rob2,i,i+1.........]
        temp = max(i + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2

#Link: https://leetcode.com/problems/house-robber/