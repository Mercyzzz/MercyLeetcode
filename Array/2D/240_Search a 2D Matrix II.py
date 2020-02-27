class Solution(object):
    def searchMatrix(self, array, target):
        """
        :type array: List[List[int]]
        :type target: int
        :rtype: bool
        """
        x = len(array) - 1
        y = 0
        while y < len(array[0]) and x >= 0:
            if target > array[x][y]:
                y += 1
            elif target < array[x][y]:
                x -= 1
            else:
                return True
        return False


print Solution().searchMatrix(
    [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
20)
