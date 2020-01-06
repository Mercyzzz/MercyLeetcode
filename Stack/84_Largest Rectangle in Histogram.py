class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        stack = [-1]
        cur = 0
        maxArea = 0
        heights.append(0)
        while cur < len(heights):
            while stack and heights[cur] < heights[stack[-1]]:
                top = stack.pop()
                height = heights[top]
                if not stack:
                    maxArea = max(maxArea, height)
                    break
                width = cur - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(cur)
            cur += 1
        return maxArea

        # heights.append(0)  # area, stack = 0, [-1]  # for i in range(len(heights)):  #     while stack and heights[stack[-1]] > heights[i]:  #         topIdx = stack.pop()  #         curHeight = heights[topIdx]  #         width = i - stack[-1] - 1  #         area = max(area, width * curHeight)  #     stack.append(i)  # return area


print Solution().largestRectangleArea([5,4,1,2])
