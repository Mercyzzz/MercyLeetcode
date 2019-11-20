class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if len(s) > (4 - len(path)) * 3:
            return
        if not s and len(path) == 4:
            res.append('.'.join(path))
            return
        for i in range(min(3, len(s))):
            curr = s[:i + 1]
            if (curr[0] == '0' and len(curr) > 1) or int(curr) > 255:
                continue
            self.dfs(s[i + 1:], path + [s[:i + 1]], res)

print Solution().restoreIpAddresses("25525511135")