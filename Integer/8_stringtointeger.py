class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        strNum = 0
        if len(str) == 0:
            return strNum

        positive = True
        if str[0] == '+' or str[0] == '-':
            if str[0] == '-':
                positive = False
            str = str[1:]

        for char in str:
            if char >= '0' and char <= '9':
                strNum = strNum * 10 + ord(char) - ord('0')
            if char < '0' or char > '9':
                break

        if strNum > 2147483647:
            if positive == False:
                return -2147483648
            else:
                return 2147483647
        if not positive:
            strNum = 0 - strNum
        return strNum