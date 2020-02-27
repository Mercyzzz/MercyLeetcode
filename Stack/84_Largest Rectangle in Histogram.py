class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = [-1]
        heights.append(0)
        maxArea = 0
        for cur in range(len(heights)):
            while heights[cur] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = cur - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(cur)
        return maxArea

print Solution().largestRectangleArea([5,4,1,2])
