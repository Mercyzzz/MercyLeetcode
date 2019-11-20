class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if self.dfs(i, j, word, board):
                    return True
        return False

    def dfs(self, i, j, word, board):
        if len(word) == 0:
            return True
        if i < 0 or i > len(board) - 1 or j < 0 or j > len(board[0]) - 1 or board[i][j] != word[0]:
            return False
        c = board[i][j]
        board[i][j] = '*'
        res = self.dfs(i - 1, j, word[1:], board) \
              or self.dfs(i + 1, j, word[1:], board) \
              or self.dfs(i, j - 1, word[1:],board) \
              or self.dfs(i, j + 1, word[1:], board)
        board[i][j] = c
        return res


print Solution().exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCB')
