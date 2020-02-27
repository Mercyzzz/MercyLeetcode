from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dq = deque()
        res = []
        for i in range(len(nums)):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            if dq[0] <= i - k:
                dq.popleft()
            if i + 1 >= k:
                res.append(nums[dq[0]])

        return res

print Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
