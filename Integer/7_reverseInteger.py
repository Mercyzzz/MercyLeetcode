class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        stack = []
        pos = 0
        neg = False
        if x < 0:
            neg = True
            x = abs(x)
        while x:
            stack.append(x % 10)
            x = x // 10
        tep = 0
        while stack:
            tep += stack.pop() * pow(10, pos)
            pos += 1
        if tep > pow(2,31) - 1:
            return 0
        return -tep if neg else tep


print Solution().reverse(-120)
