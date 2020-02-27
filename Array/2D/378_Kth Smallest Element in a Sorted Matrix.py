class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        left = matrix[0][0]
        right = matrix[-1][-1]
        while left < right:
            mid = (left + right) / 2
            cnt = 0
            for i in range(len(matrix)):
                rowLeft, rowRight = 0, len(matrix[0])
                while rowLeft < rowRight:
                    rowMid = (rowLeft + rowRight) / 2
                    if matrix[i][rowMid] < mid:
                        rowLeft = rowMid + 1
                    else:
                        rowRight = rowMid
                cnt += rowLeft
            print left, right, mid, cnt
            if cnt < k:
                left = mid + 1
            else:
                right = mid
        return right

print Solution().kthSmallest([
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
], 8)
