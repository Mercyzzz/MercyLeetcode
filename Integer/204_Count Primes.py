import math


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        prime = [True] * n
        for i in range(2, n):
            if not prime[i]:
                continue
            res += 1
            for j in range(2 * i, n, i):
                prime[j] = False
        return res


print Solution().countPrimes(499979)
