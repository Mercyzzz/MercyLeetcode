class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                cnt = self.count(i, j, board)
                if cnt < 2 and board[i][j] == 1:
                    board[i][j] = -1
                elif cnt == 3 and board[i][j] == 0:
                    board[i][j] = 2
                elif cnt >= 4 and board[i][j] == 1:
                    board[i][j] = -1
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == -1:
                    board[i][j] = 0
                if board[i][j] == 2:
                    board[i][j] = 1

    def count(self, i, j, board):
        rowBound = [i - 1, i, i + 1]
        colBound = [j - 1, j, j + 1]
        cnt = 0
        for row in rowBound:
            for col in colBound:
                if row == i and col == j:
                    continue
                if row >= 0 and row < len(board) and col >= 0 and col < len(board[0]) and (
                        board[row][col] == 1 or board[row][col] == -1):
                    cnt += 1
        return cnt

a = [[0,0,0,0,0,0],
     [0,0,0,0,0,0],
     [0,0,1,1,1,0],
     [0,1,1,1,0,0],
     [0,0,0,0,0,0],
     [0,0,0,0,0,0]]

print Solution().gameOfLife(a)
print a
