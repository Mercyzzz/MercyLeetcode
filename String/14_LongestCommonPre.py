class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        ret = ''
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if len(strs[j]) - 1 < i or strs[j][i] != char:
                    return ret
            ret += char
        return ret


print Solution().longestCommonPrefix(["aa","a"])
