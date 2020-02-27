class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        cnt = 0
        res = []
        for i in range(num + 1):
            while i != 0:
                i = i & i - 1
                cnt += 1
            res.append(cnt)
            cnt = 0
        return res

print Solution().countBits(5)