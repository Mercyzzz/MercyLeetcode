class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        x = len(matrix) - 1
        y = 0
        while y < len(matrix[0]) and x >= 0:
            if target > matrix[x][y]:
                y += 1
            elif target < matrix[x][y]:
                x -= 1
            else:
                return True
        return False


print Solution().searchMatrix(
    [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
20)
