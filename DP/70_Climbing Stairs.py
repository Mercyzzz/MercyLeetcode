class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        dp = [0 for i in range (n)]
        dp[0], dp[1] = 1,2
        for i in range(2,n):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[-1]
print Solution().climbStairs(4)