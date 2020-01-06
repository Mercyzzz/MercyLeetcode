class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        r1, r2, c1, c2 = 0, len(matrix) - 1, 0, len(matrix[0] - 1)
        res = []
        while r1 < r2 and c1 < c2:
            for i in range(c1, c2):
                res.append(matrix[r1][i])
            for i in range(r1, r2):
                res.append(matrix[i][c2])