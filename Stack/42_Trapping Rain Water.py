class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = cur = 0
        stack = []
        while cur < len(height):
            while stack and height[cur] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                distance = cur - stack[-1] - 1
                boHi = min(height[cur], height[stack[-1]]) - height[top]
                ans += distance * boHi
            stack.append(cur)
            cur += 1
        return ans


print Solution().trap([3, 2, 1, 5])
