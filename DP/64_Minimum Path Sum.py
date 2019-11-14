class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [i for i in grid[0]]
        for i in range(1,len(dp)):
            dp[i] = dp[i - 1] + grid[0][i]
        dp = [dp for i in range(2)]
        for i in range(1, len(grid)):
            for j in range(len(grid[0])):
                if j == 0:
                    dp[1][j] = dp[0][j] + grid[i][j]
                else:
                    dp[1][j] = min((dp[0][j] + grid[i][j]), (dp[1][j - 1] + grid[i][j]))
                    dp[0][j] = dp[1][j]
        return dp[1][-1]


print Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
