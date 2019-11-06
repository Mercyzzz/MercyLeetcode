class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
        result = ''
        cycleLen = 2 * numRows - 2;
        n = len(s)
        for i in range(0, numRows):
            j = 0
            while j + i < n:
                result += s[i + j]  # print straight column item
                if i != 0 and i != numRows - 1 and j + cycleLen - i < n:
                    result += s[j + cycleLen - i]  # print zigzag column item
                j += cycleLen
        return result


print Solution().convert('PAYPALISHIRING', 4)
