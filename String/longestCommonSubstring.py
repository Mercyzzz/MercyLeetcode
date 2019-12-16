class Solution(object):
    def longestCommonSubstring(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        maxL = - 1
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0
                maxL = max(maxL, dp[i][j])
        return maxL

print Solution().longestCommonSubstring('abc','abc')