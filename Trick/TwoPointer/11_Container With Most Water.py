class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxArea = 0
        while left < right:
            maxArea = max(min(height[left], height[right]) * (right - left), maxArea)
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1

        return maxArea


print Solution().maxArea([2, 3, 4, 5, 18, 17, 6])
