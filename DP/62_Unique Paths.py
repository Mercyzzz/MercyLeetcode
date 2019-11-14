class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1] * m for i in range(2)]
        for i in range(1, n):
            for j in range(1, m):
                dp[1][j] = dp[0][j] + dp[1][j - 1]
                dp[0][j] = dp[1][j]
        return dp[1][-1]


print Solution().uniquePaths(7, 3)
