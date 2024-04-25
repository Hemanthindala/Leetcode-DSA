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
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        



Leetcode: https://leetcode.com/problems/longest-ideal-subsequence/
