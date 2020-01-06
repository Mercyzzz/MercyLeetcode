class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        hashN = {n}
        while n != 1:
            sumN = 0
            while n != 0:
                remainder = n % 10
                sumN += remainder * remainder
                n = n // 10
            if sumN in hashN:
                return False
            else:
                n = sumN
                hashN.add(n)
        return True

print Solution().isHappy(11)