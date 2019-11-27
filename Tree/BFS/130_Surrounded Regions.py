class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1):
                    board[i][j] = '*'
                    self.bfs(board, [(i, j)])
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '*':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'


    def bfs(self, board, cur):
        next = []
        while cur:
            for item in cur:
                i, j = item
                if i > 0 and board[i - 1][j] == 'O':
                    board[i - 1][j] = '*'
                    next.append((i - 1, j))
                if i < len(board) - 1 and board[i + 1][j] == 'O':
                    board[i + 1][j] = '*'
                    next.append((i + 1, j))
                if j > 0 and board[i][j - 1] == 'O':
                    board[i][j - 1] = '*'
                    next.append((i, j - 1))
                if j < len(board[0]) - 1 and board[i][j + 1] == 'O':
                    board[i][j + 1] = '*'
                    next.append((i, j + 1))
            cur = next
            next = []


a = [
    ["X","O","X","X"],
    ["O","X","O","X"],
    ["X","O","X","O"],
    ["O","X","O","X"],
    ["X","O","X","O"],
    ["O","X","O","X"]
]

print Solution().solve(a)
print a
