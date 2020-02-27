class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == [] : return []
        res = []
        maxUp = maxLeft = 0
        maxDown = len(matrix) - 1
        maxRight = len(matrix[0]) - 1
        direction = 0 # 0 go right, 1 go down, 2 go left, 3 up
        while True:
            if direction == 0: #go right
                for i in range(maxLeft, maxRight+1):
                    res.append(matrix[maxUp][i])
                maxUp += 1
            elif direction == 1: # go down
                for i in range(maxUp, maxDown+1):
                    res.append(matrix[i][maxRight])
                maxRight -= 1
            elif direction == 2: # go left
                for i in reversed(range(maxLeft, maxRight+1)):
                    res.append(matrix[maxDown][i])
                maxDown -= 1
            else: #go up
                for i in reversed(range(maxUp, maxDown+1)):
                    res.append(matrix[i][maxLeft])
                maxLeft +=1
            if maxUp > maxDown or maxLeft > maxRight:
                return res
            direction = (direction + 1 ) % 4

print Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]])