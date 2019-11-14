class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid[0])
        n = len(obstacleGrid)
        dp = [1] * m
        for i in range(m):
            if i == 0 and obstacleGrid[0][0] == 1:
                dp[i] = 0
            if dp[i - 1] == 0 or obstacleGrid[0][i] == 1:
                dp[i] = 0
        dp = [dp for i in range(2)]
        for i in range(1, n):
            for j in range(0, m):
                if obstacleGrid[i][j] == 1:
                    dp[1][j] = 0
                    dp[0][j] = 0
                    continue
                if j == 0:
                    dp[1][j] = dp[0][j]
                else:
                    dp[1][j] = dp[0][j] + dp[1][j - 1]
                    dp[0][j] = dp[1][j]
        return dp[1][-1]


print Solution().uniquePathsWithObstacles([[1, 0]])
