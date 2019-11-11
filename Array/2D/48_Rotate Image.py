class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in range(length // 2):
            for j in range(i, length - 1 - i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[length - 1 - j][i]
                matrix[length - 1 - j][i] = matrix[length - 1 - i][length - 1 - j]
                matrix[length - 1 - i][length - 1 - j] = matrix[j][length - 1 - i]
                matrix[j][length - 1 - i] = tmp


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print Solution().rotate(a)
print a
