class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        left, right, length = 0, 0, 0
        dp = [[False for i in range(len(s))] for i in range(len(s))]
        for i in range(len(dp)):
            dp[i][i] = True
            if i + 1 < len(s) and s[i] == s[i + 1]:
                dp[i][i + 1] = True
        for i in range(len(dp)):
            for j in range(i + 1, len(dp[0])):
                if i + 1 < len(s) and j - 1 >= 0:
                    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                if dp[i][j] and j - i > length:
                    left, right, length = i, j, j - i
        return s[left:right + 1]


print Solution().longestPalindrome('babad')
