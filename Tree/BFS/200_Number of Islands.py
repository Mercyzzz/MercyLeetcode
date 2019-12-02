class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    cnt += 1
                    grid[i][j] = 2
                    self.bfs(grid, i, j)
        return cnt

    def bfs(self, grid, i, j):
        if i > 0 and grid[i - 1][j] == '1':
            grid[i - 1][j] = 2
            self.bfs(grid, i - 1, j)
        if i < len(grid) - 1 and grid[i + 1][j] == '1':
            grid[i + 1][j] = 2
            self.bfs(grid, i + 1, j)
        if j > 0 and grid[i][j - 1] == '1':
            grid[i][j - 1] = 2
            self.bfs(grid, i, j - 1)
        if j < len(grid[0]) - 1 and grid[i][j + 1] == '1':
            grid[i][j + 1] = 2
            self.bfs(grid, i, j + 1)


print Solution().numIslands(
    [["1", "1", "0", "0", "0"],
     ["1", "1", "0", "0", "0"],
     ["0", "0", "1", "0", "0"],
     ["0", "0", "0", "1", "1"]])
