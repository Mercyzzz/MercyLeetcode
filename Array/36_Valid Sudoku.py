class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [[False] * 9 for j in range(9)]
        col = [[False] * 9 for j in range(9)]
        block = [[False] * 9 for j in range(9)]
        