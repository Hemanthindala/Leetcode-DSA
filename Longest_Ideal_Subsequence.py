class Solution(object):
    def longestIdealString(self, s, k):
        dp=[0]*26
        ans=1
        for i in range(len(s)):
            element=ord(s[i])-ord('a')
            j=element
            while(j>=0 and j>=element-k):
                dp[element]=max(dp[j]+1,dp[element])
                j=j-1  
            j=element+1     
            while(j<26 and j<=element+k):
                dp[element]=max(dp[j]+1,dp[element])
                j=j+1     
            ans=max(ans,dp[element])
        return ans      

#  First we will create an array of size 26 with all 0's
# Then we consider checking only the elements of difference k
# Let k=2
# for c=2 we check only the value of c=2,c=1,c=0 on left and c=3, c=4 on right i.e from element-k to element+k
#
# And why ans=1 is initialized because if string = az which means we can't find any letters with difference <=k
# then the ans should be 1 right. So that's the reason





# Leetcode: https://leetcode.com/problems/longest-ideal-subsequence/
