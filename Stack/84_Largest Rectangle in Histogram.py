class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        area, stack = 0, [-1]
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                topIdx = stack.pop()
                curHeight = heights[topIdx]
                width = i - stack[-1] - 1
                area = max(area, width * curHeight)
            stack.append(i)
        return area


print Solution().largestRectangleArea([1,2,3,4,3,2,6])
