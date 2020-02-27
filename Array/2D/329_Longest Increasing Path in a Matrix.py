class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        self.paths = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        if not matrix or not matrix[0]:
            return 0
        cache = [[0] * len(matrix[0]) for i in range(len(matrix))]
        res = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(self.dfs(matrix, i, j, cache), res)
        return res

    def dfs(self, matrix, i, j, memo):
        if memo[i][j] != 0:
            return memo[i][j]
        maxN = 1
        for path in self.paths:
            x = i + path[0]
            y = j + path[1]
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[i][j] > matrix[x][y]:
                maxN = max(maxN, self.dfs(matrix, x, y, memo) + 1)
        memo[i][j] = maxN
        return maxN


print Solution().longestIncreasingPath([
  [9,8,4],
  [6,7,8],
] )
