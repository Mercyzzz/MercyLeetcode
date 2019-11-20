class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0 for i in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 0 if s[i - 1] == 0 else 1
        for i in range(2, len(s) + 1):
            if int(s[i - 2: i]) <= 26 and int(s[i - 2:i]) >= 10:
                dp[i] += dp[i - 2]
            if s[i - 1] != 0:
                dp[i] += dp[i - 1]
        return dp[len(s)]


print Solution().numDecodings('226')
