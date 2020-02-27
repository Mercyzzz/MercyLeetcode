class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n > 0 and n % 4 == 0:
            n /= 4
        if (n % 8 == 7):
            return 4
        res = n
        i = 2
        while i * i <= n:
            a = n / (i * i)
            b = n % (i * i)
            res = min(res, a + self.numSquares(b))
            i += 1
        return res


print Solution().numSquares(13)
