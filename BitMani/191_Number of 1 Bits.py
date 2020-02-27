class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(32):
            res += n & 1
            n = n >> 1
        return res

print Solution().hammingWeight(6)