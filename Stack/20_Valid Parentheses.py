class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i in ('(', '[', '{'):
                stack.append(i)
                continue
            if not stack:
                return False
            top = stack.pop()
            if (i == ')' and top != '(') or \
                    (i == ']' and top != '[') or \
                    (i == '}' and top != '{'):
                return False
        return False if stack else True

print Solution().isValid(']')